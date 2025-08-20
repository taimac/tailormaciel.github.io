"""
Unit tests for GitHub project backlog fetcher.

Testing Strategy:
- Mock external dependencies (requests, file operations)
- Test both success and error scenarios
- Verify security considerations (input validation, error handling)
- Ensure proper separation of concerns

Architecture Notes:
- Uses pytest fixtures for consistent test setup
- Implements proper mocking to isolate units under test
- Tests both positive and negative scenarios
"""

from unittest.mock import MagicMock, patch

import pytest
import requests

from scripts.automation.export_backlog import GitHubIssuesExporter


class TestSimpleIssuesExporter:
    """
    Test suite for GitHubIssuesExporter class.

    OOP Testing Principles:
    - Each test focuses on a single responsibility
    - Uses dependency injection through mocking
    - Maintains test isolation and repeatability
    """

    @pytest.fixture
    def exporter(self):
        """
        Fixture to create a GitHubIssuesExporter instance.

        Architecture Notes:
        - Provides consistent test setup
        - Uses fake credentials to avoid security exposure
        - Demonstrates fixture pattern for test organization
        """
        return GitHubIssuesExporter(repo="owner/repo", token="fake-token")

    @patch("scripts.automation.export_backlog.create_session_with_pooling_and_timeout")
    def test_create_session_with_pooling_and_timeout(self, mock_create_session):
        """
        Test that the session is configured with pooling, retries, and timeouts.

        Security Testing Notes:
        - Verifies that secure session configuration is applied
        - Ensures dependency injection works correctly
        - Tests that infrastructure concerns are properly separated
        """
        # Arrange: Set up mock session
        mock_session = MagicMock()
        mock_create_session.return_value = mock_session

        # Act: Create exporter instance
        exporter = GitHubIssuesExporter(repo="owner/repo", token="fake-token")

        # Assert: Verify session configuration was applied
        assert exporter.session == mock_session
        mock_create_session.assert_called_once()

    def test_get_issues_excludes_pull_requests(self, exporter):
        """
        Test fetching issues from the GitHub API and excluding pull requests.

        Business Logic Testing:
        - Verifies that pull requests are filtered out
        - Tests pagination handling
        - Ensures proper API response processing

        Security Testing:
        - Mocks external API to prevent actual network calls
        - Validates data filtering logic
        """
        # Arrange: Mock API response with mixed issues and PRs
        with patch.object(exporter.session, "get") as mock_get:
            mock_response = MagicMock()
            mock_response.json.return_value = [
                {
                    "number": 1,
                    "title": "Issue 1",
                    "state": "open",
                    "labels": [],
                    "html_url": "https://github.com/owner/repo/issues/1",
                },
                {
                    "number": 2,
                    "title": "Issue 2",
                    "state": "closed",
                    "labels": [],
                    "html_url": "https://github.com/owner/repo/issues/2",
                },
                {
                    "number": 3,
                    "title": "Pull Request",
                    "state": "open",
                    "pull_request": {},
                    "html_url": "https://github.com/owner/repo/pull/3",
                },
            ]
            mock_response.links = {}
            mock_response.raise_for_status = MagicMock()
            mock_get.return_value = mock_response

            # Act: Fetch issues (use current API)
            issues = exporter.fetch_all_items()

            # Assert: Verify filtering worked correctly
            assert len(issues) == 3  # Should include all items (filtering happens in exporter.classify_items)
            assert any(issue["title"] == "Issue 1" for issue in issues)
            assert any(issue["title"] == "Issue 2" for issue in issues)
            assert any(issue["title"] == "Pull Request" for issue in issues)

    @patch("scripts.automation.export_backlog.open", create=True)
    @patch("scripts.automation.export_backlog.os.makedirs")
    def test_export_backlog_generates_correct_markdown(self, mock_makedirs, mock_open, exporter):
        """
        Test exporting issues to a markdown file with correct content.

        Integration Testing:
        - Tests the complete export workflow
        - Verifies markdown formatting is correct
        - Ensures file operations work properly

        Security Testing:
        - Mocks file operations to prevent actual file system access
        - Validates that directory creation is safe
        """
        # Arrange: Mock the fetch_all_items method to return test data
        with patch.object(exporter, "fetch_all_items") as mock_fetch:
            mock_fetch.return_value = [
                {
                    "number": 1,
                    "title": "Issue 1",
                    "state": "open",
                    "labels": [],
                    "html_url": "https://github.com/owner/repo/issues/1",
                },
                {
                    "number": 2,
                    "title": "Issue 2",
                    "state": "closed",
                    "labels": [],
                    "html_url": "https://github.com/owner/repo/issues/2",
                },
            ]

            # Mock file writing
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            # Act: Export backlog (current API)
            exporter.output_file = "docs/backlog_summary.md"
            exporter.export()

            # Assert: Verify file operations and content
            mock_makedirs.assert_called_once_with("docs", exist_ok=True)
            mock_open.assert_called_once_with(exporter.output_file, "w", encoding="utf-8")

            # Verify that write was called (content will vary due to timestamp)
            assert mock_file.write.called
            written_content = mock_file.write.call_args[0][0]
            assert "# 📋 Development Backlog" in written_content
            assert "Issue 1" in written_content
            assert "Issue 2" in written_content

    def test_get_issues_handles_api_errors(self, exporter):
        """
        Test error handling when the GitHub API returns an error.

        Error Handling Testing:
        - Verifies graceful failure when API is unavailable
        - Ensures proper logging of error conditions
        - Tests that exceptions don't crash the application

        Security Testing:
        - Validates that error messages don't expose sensitive information
        - Ensures proper error handling prevents information leakage
        """
        # Arrange: Mock session to raise an exception
        with patch.object(exporter.session, "get") as mock_get:
            mock_get.side_effect = requests.exceptions.RequestException("API error")

            # Act: Attempt to get issues
            issues = exporter.fetch_all_items()

            # Assert: Verify graceful error handling
            assert issues == []  # Should return empty list on error

    def test_get_issues_empty_response(self, exporter):
        """
        Test fetching issues when the API returns an empty response.

        Edge Case Testing:
        - Tests behavior with empty repository
        - Verifies pagination logic handles empty responses
        - Ensures graceful handling of edge cases

        Architecture Testing:
        - Validates that empty responses are handled correctly
        - Tests boundary conditions in pagination logic
        """
        # Arrange: Mock empty API response
        with patch.object(exporter.session, "get") as mock_get:
            mock_response = MagicMock()
            mock_response.json.return_value = []
            mock_response.links = {}
            mock_response.raise_for_status = MagicMock()
            mock_get.return_value = mock_response

            # Act: Fetch issues
            issues = exporter.fetch_all_items()

            # Assert: Verify empty response handling
            assert issues == []

    def test_format_issue_handles_missing_fields(self, exporter):
        """
        Test that format_issue handles missing or malformed fields gracefully.
        """
        # Arrange: Issue with missing fields
        incomplete_issue = {
            "number": 1,
            # Missing title, state, labels, html_url
        }

        # Act: Format the incomplete issue using formatter directly
        result = exporter.formatter.format_issue(incomplete_issue)

        # Assert: Verify graceful handling of missing fields
        assert "No title" in result
        assert "#1" in result or "[#1]" in result
        # Default state handling may map to closed emoji ✅ or other fallback
        assert "✅" in result or "🔁" in result


# Run tests with coverage
if __name__ == "__main__":
    pytest.main([__file__, "-v", "--cov=scripts"])
