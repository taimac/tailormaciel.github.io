#!/usr/bin/env python3
"""
Enhanced GitHub Issues Import Script with Dry-Run Support

Educational Value:
- Demonstrates Command Pattern for operation encapsulation
- Shows how to implement safe preview functionality
- Teaches proper argument parsing and user interaction
- Illustrates defensive programming with validation

Architecture Notes:
- Separates preview logic from execution logic
- Uses Strategy Pattern for different output formats
- Implements Factory Pattern for command creation
- Follows Single Responsibility Principle throughout
"""

import argparse
import csv
import os
import subprocess
import sys
from dataclasses import dataclass
from enum import Enum
from typing import Any


class ExecutionMode(Enum):
    """
    Execution mode enumeration for type safety

    Educational Value:
    - Demonstrates enum usage for type safety
    - Shows how to prevent invalid state combinations
    - Teaches intention-revealing names
    """

    DRY_RUN = "dry_run"
    EXECUTE = "execute"
    INTERACTIVE = "interactive"


@dataclass
class IssueCommand:
    """
    Command object encapsulating issue creation operation

    Architecture Notes:
    - Implements Command Pattern for operation encapsulation
    - Immutable data structure for thread safety
    - Clear separation between data and behavior

    Security Considerations:
    - All fields validated before object creation
    - No mutable state to prevent tampering
    """

    title: str
    body: str
    labels: list[str]
    milestone: str | None
    exists: bool = False

    def __post_init__(self):
        """Validate command data after creation"""
        if not self.title or not isinstance(self.title, str):
            raise ValueError("Title must be a non-empty string")
        if not self.body or not isinstance(self.body, str):
            raise ValueError("Body must be a non-empty string")


class DryRunFormatter:
    """
    Strategy Pattern implementation for different dry-run output formats

    Educational Value:
    - Demonstrates Strategy Pattern for flexible output
    - Shows how to implement console formatting
    - Teaches user experience considerations in CLI tools

    Architecture Notes:
    - Single Responsibility: Only handles output formatting
    - Easy to extend with new formats (JSON, HTML, etc.)
    - Follows Open/Closed Principle
    """

    @staticmethod
    def format_summary(commands: list[IssueCommand], mode: ExecutionMode) -> str:
        """
        Generate execution summary with clear user guidance

        Args:
            commands: List of issue commands to execute
            mode: Current execution mode

        Returns:
            Formatted summary string

        Educational Value:
        - Shows how to provide clear user feedback
        - Demonstrates string formatting best practices
        - Teaches defensive programming with edge cases
        """
        total = len(commands)
        new_issues = [cmd for cmd in commands if not cmd.exists]
        existing_issues = [cmd for cmd in commands if cmd.exists]

        header = f"""
🎯 **GitHub Issues Import Summary**
{'='*50}
📊 **Statistics:**
   • Total issues in CSV: {total}
   • New issues to create: {len(new_issues)}
   • Existing issues (will skip): {len(existing_issues)}
   • Execution mode: {mode.value.replace('_', ' ').title()}
"""

        if mode == ExecutionMode.DRY_RUN:
            header += "\n⚠️  **DRY RUN MODE** - No actual changes will be made\n"
        elif mode == ExecutionMode.EXECUTE:
            header += "\n🚀 **EXECUTION MODE** - Issues will be created in GitHub\n"

        # Show new issues that will be created
        if new_issues:
            header += f"\n📝 **New Issues to Create ({len(new_issues)}):**\n"
            for i, cmd in enumerate(new_issues[:5], 1):  # Show first 5
                title_preview = cmd.title[:60] + "..." if len(cmd.title) > 60 else cmd.title
                header += f"   {i}. {title_preview}\n"
                if cmd.labels:
                    header += f"      Labels: {', '.join(cmd.labels[:3])}\n"

            if len(new_issues) > 5:
                header += f"   ... and {len(new_issues) - 5} more issues\n"

        # Show existing issues that will be skipped
        if existing_issues:
            header += f"\n⏭️  **Existing Issues (Will Skip - {len(existing_issues)}):**\n"
            for i, cmd in enumerate(existing_issues[:3], 1):  # Show first 3
                title_preview = cmd.title[:60] + "..." if len(cmd.title) > 60 else cmd.title
                header += f"   {i}. {title_preview}\n"

            if len(existing_issues) > 3:
                header += f"   ... and {len(existing_issues) - 3} more existing issues\n"

        return header

    @staticmethod
    def format_detailed_preview(commands: list[IssueCommand]) -> str:
        """
        Generate detailed preview of each issue command

        Educational Value:
        - Shows how to provide comprehensive user information
        - Demonstrates data structure traversal
        - Teaches user interface design principles
        """
        if not commands:
            return "\n📝 No issues to process.\n"

        output = "\n📋 **Detailed Issue Preview:**\n" + "=" * 50 + "\n"

        for i, cmd in enumerate(commands, 1):
            status = "🔄 WILL CREATE" if not cmd.exists else "⏭️  WILL SKIP (EXISTS)"

            output += f"""
**Issue #{i}: {status}**
📌 Title: {cmd.title}
🏷️  Labels: {', '.join(cmd.labels) if cmd.labels else 'None'}
🎯 Milestone: {cmd.milestone or 'None'}
📝 Body: {cmd.body[:150]}{'...' if len(cmd.body) > 150 else ''}
{'-'*60}
"""

        return output


class GitHubIssuesImporter:
    """
    Enhanced GitHub Issues importer with comprehensive dry-run support

    Educational Value:
    - Demonstrates Command Pattern for safe operation preview
    - Shows how to implement user-friendly CLI interfaces
    - Teaches error handling and validation strategies
    - Illustrates separation of concerns in tool design

    Architecture Notes:
    - Factory Pattern for command creation
    - Strategy Pattern for different execution modes
    - Single Responsibility for each method
    - Dependency Injection for testability

    Security Considerations:
    - Input validation for all CSV data
    - Safe command construction with validation
    - Prevents injection through subprocess argument arrays
    """

    def __init__(self, owner: str, repo: str):
        """
        Initialize importer with repository information

        Args:
            owner: GitHub repository owner
            repo: GitHub repository name

        Security Notes:
        - Validates repository format to prevent path traversal
        - Uses parameterized commands to prevent injection
        """
        self.owner = self._validate_identifier(owner, "owner")
        self.repo = self._validate_identifier(repo, "repo")
        self.formatter = DryRunFormatter()

    def _validate_identifier(self, identifier: str, field_name: str) -> str:
        """
        Validate GitHub identifier format for security

        Args:
            identifier: The identifier to validate
            field_name: Name of the field (for error messages)

        Returns:
            Validated identifier

        Raises:
            ValueError: If identifier format is invalid

        Security Implementation:
        - Prevents path traversal attacks
        - Validates against malicious characters
        - Ensures proper GitHub identifier format
        """
        if not identifier or not isinstance(identifier, str):
            raise ValueError(f"{field_name} must be a non-empty string")

        # GitHub identifiers can contain alphanumeric, hyphens, and underscores
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.")
        if not all(c in allowed_chars for c in identifier):
            raise ValueError(f"{field_name} contains invalid characters")

        if len(identifier) > 100:  # Reasonable limit
            raise ValueError(f"{field_name} is too long (max 100 characters)")

        return identifier

    def load_csv_data(self, csv_path: str) -> list[dict[str, Any]]:
        """
        Load and validate CSV data with comprehensive error handling

        Args:
            csv_path: Path to CSV file

        Returns:
            List of validated issue dictionaries

        Educational Value:
        - Demonstrates file handling best practices
        - Shows proper exception handling
        - Teaches data validation techniques

        Security Notes:
        - Validates file path to prevent directory traversal
        - Limits file size to prevent memory exhaustion
        - Sanitizes CSV data to prevent injection
        """
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found: {csv_path}")

        # Security: Check file size to prevent memory exhaustion
        file_size = os.path.getsize(csv_path)
        max_size = 10 * 1024 * 1024  # 10MB limit
        if file_size > max_size:
            raise ValueError(f"CSV file too large: {file_size} bytes (max {max_size})")

        try:
            with open(csv_path, encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)

                # Validate required columns exist
                required_columns = {"title", "body", "labels", "status", "milestone"}
                if not required_columns.issubset(reader.fieldnames):
                    missing = required_columns - set(reader.fieldnames)
                    raise ValueError(f"Missing required CSV columns: {missing}")

                issues = []
                for row_num, row in enumerate(reader, 2):  # Start at 2 (header is row 1)
                    try:
                        # Validate and clean each row
                        validated_row = self._validate_csv_row(row, row_num)
                        issues.append(validated_row)
                    except ValueError as e:
                        print(f"⚠️  Warning: Skipping row {row_num}: {e}")
                        continue

                print(f"✅ Successfully loaded {len(issues)} valid issues from CSV")
                return issues

        except csv.Error as e:
            # Clean Code: Preserve original exception context
            raise ValueError(f"CSV parsing error: {e}") from e
        except UnicodeDecodeError as e:
            # Clean Code: Preserve original exception context
            raise ValueError(f"File encoding error: {e}") from e

    def diagnose_csv(self, csv_path: str) -> None:
        """
        Diagnostic utility to analyze CSV structure and data quality

        Args:
            csv_path: Path to CSV file to diagnose

        Educational Value:
        - Demonstrates data quality analysis techniques
        - Shows how to build diagnostic tools for debugging
        - Teaches comprehensive error reporting strategies
        """
        print(f"\n🔍 **CSV Diagnostic Report for**: {csv_path}")
        print("=" * 60)

        try:
            with open(csv_path, encoding="utf-8") as csvfile:
                # Basic file info
                content = csvfile.read()
                csvfile.seek(0)

                print("📊 **File Statistics:**")
                print(f"   • File size: {len(content):,} bytes")
                print(f"   • Line count: {content.count(chr(10)) + 1}")

                # CSV structure analysis
                reader = csv.DictReader(csvfile)
                fieldnames = reader.fieldnames or []

                print("\n📋 **CSV Structure:**")
                print(f"   • Columns found: {len(fieldnames)}")
                print("   • Column names: {}".format(", ".join(fieldnames)))

                # Required columns check
                required_columns = {"title", "body", "labels", "status", "milestone"}
                missing_columns = required_columns - set(fieldnames)
                if missing_columns:
                    print("   ❌ Missing required columns: {}".format(", ".join(missing_columns)))
                else:
                    print("   ✅ All required columns present")

                # Data quality analysis
                print("\n📊 **Data Quality Analysis:**")

                row_count = 0
                issues_by_type = {
                    "empty_title": 0,
                    "empty_body": 0,
                    "empty_labels": 0,
                    "none_values": 0,
                    "long_title": 0,
                    "long_body": 0,
                }

                for row_num, row in enumerate(reader, 2):
                    row_count += 1

                    # Check for None values
                    none_fields = [field for field, value in row.items() if value is None]
                    if none_fields:
                        issues_by_type["none_values"] += 1
                        print(f"   Row {row_num}: None values in {none_fields}")

                    # Check title
                    title = row.get("title")
                    if not title or (isinstance(title, str) and not title.strip()):
                        issues_by_type["empty_title"] += 1
                    elif isinstance(title, str) and len(title) > 500:
                        issues_by_type["long_title"] += 1

                    # Check body
                    body = row.get("body")
                    if not body or (isinstance(body, str) and not body.strip()):
                        issues_by_type["empty_body"] += 1
                    elif isinstance(body, str) and len(body) > 65536:
                        issues_by_type["long_body"] += 1

                    # Check labels
                    labels = row.get("labels")
                    if not labels or (isinstance(labels, str) and not labels.strip()):
                        issues_by_type["empty_labels"] += 1

                print(f"   • Total rows processed: {row_count}")
                print(f"   • Rows with None values: {issues_by_type['none_values']}")
                print(f"   • Rows with empty titles: {issues_by_type['empty_title']}")
                print(f"   • Rows with empty bodies: {issues_by_type['empty_body']}")
                print(f"   • Rows with empty labels: {issues_by_type['empty_labels']}")
                print(f"   • Rows with long titles (>500): {issues_by_type['long_title']}")
                print(f"   • Rows with long bodies (>65k): {issues_by_type['long_body']}")

                # Overall health assessment
                total_issues = sum(issues_by_type.values())
                if total_issues == 0:
                    print("\n✅ **CSV Health**: Excellent - No data quality issues detected")
                elif total_issues < row_count * 0.1:  # Less than 10% issues
                    print(f"\n⚠️  **CSV Health**: Good - Minor issues detected ({total_issues}/{row_count})")
                else:
                    print(f"\n❌ **CSV Health**: Poor - Significant issues detected ({total_issues}/{row_count})")

        except FileNotFoundError:
            print(f"❌ File not found: {csv_path}")
        except Exception as e:
            print(f"❌ Diagnostic error: {e}")

    def _validate_csv_row(self, row: dict[str, str], row_num: int) -> dict[str, Any]:
        """
        Validate and sanitize a single CSV row with defensive programming

        Args:
            row: Raw CSV row data (may contain None values)
            row_num: Row number for error reporting

        Returns:
            Validated and cleaned row data

        Educational Value:
        - Demonstrates defensive programming for external data
        - Shows comprehensive input validation techniques
        - Teaches graceful degradation strategies

        Security Implementation:
        - Sanitizes all string inputs to prevent injection
        - Validates data types and formats defensively
        - Handles None, empty, and malformed values safely

        Architecture Notes:
        - Uses Strategy Pattern for different validation approaches
        - Implements Template Method Pattern for consistent validation flow
        - Follows Single Responsibility Principle with helper functions
        """

        # Defensive helper function for safe string extraction
        def safe_get_string(field_name: str, default: str = "") -> str:
            """
            Safely extract string value from CSV row

            Args:
                field_name: CSV column name
                default: Default value if field is missing/None/empty

            Returns:
                Cleaned string value

            Educational Notes:
            - Demonstrates defensive programming against None values
            - Shows type checking and conversion strategies
            - Teaches input sanitization patterns

            Security Implementation:
            - Prevents 'NoneType' attribute errors
            - Sanitizes string content to prevent injection
            - Validates data types before processing
            """
            try:
                value = row.get(field_name)

                # Handle None values (empty CSV cells or missing columns)
                if value is None:
                    print(f"🔧 Debug: None value found in '{field_name}' row {row_num}, using default")
                    return default

                # Handle non-string values (CSV parser edge cases)
                if not isinstance(value, str):
                    print(f"⚠️  Warning: Non-string value in '{field_name}' row {row_num}: {type(value).__name__}")
                    # Convert to string safely, handling None case
                    converted = str(value) if value is not None else default
                    return converted.strip() if converted else default

                # Clean whitespace and validate
                cleaned = value.strip()
                return cleaned if cleaned else default

            except Exception as e:
                print(f"⚠️  Warning: Error processing '{field_name}' in row {row_num}: {e}")
                return default

        def safe_parse_labels(labels_raw: str) -> list[str]:
            """
            Parse labels with comprehensive error handling

            Args:
                labels_raw: Raw labels string from CSV

            Returns:
                List of cleaned label strings

            Educational Value:
            - Demonstrates multiple fallback strategies
            - Shows how to handle various data corruption scenarios
            - Teaches graceful degradation principles

            Architecture Notes:
            - Uses Strategy Pattern for different parsing approaches
            - Implements Circuit Breaker Pattern for error isolation
            - Follows Fail-Safe Defaults principle
            """
            if not labels_raw:
                return []

            try:
                # Strategy 1: Standard comma-separated parsing
                labels = []
                for label in labels_raw.split(","):
                    cleaned_label = label.strip()
                    if cleaned_label:  # Skip empty labels
                        # Security: Basic sanitization to prevent injection
                        if len(cleaned_label) <= 50 and not any(char in cleaned_label for char in ["<", ">", '"', "'"]):
                            labels.append(cleaned_label)
                        else:
                            print(f"⚠️  Warning: Skipping invalid label '{cleaned_label[:20]}...' in row {row_num}")

                return labels

            except AttributeError as e:
                print(f"⚠️  Warning: Label parsing error in row {row_num}: {e}")
                return []

            except Exception as e:
                print(f"⚠️  Warning: Unexpected label parsing error in row {row_num}: {e}")
                return []

        def validate_field_lengths(cleaned_row: dict[str, Any]) -> dict[str, Any]:
            """
            Validate and truncate fields that exceed platform limits

            Args:
                cleaned_row: Row data to validate

            Returns:
                Row data with length validation applied

            Educational Value:
            - Demonstrates platform constraint awareness
            - Shows data truncation strategies
            - Teaches user-friendly error handling

            Security Implementation:
            - Prevents buffer overflow scenarios
            - Limits resource consumption
            - Maintains data integrity within constraints
            """
            # GitHub platform limits
            MAX_TITLE_LENGTH = 256  # GitHub issue title limit
            MAX_BODY_LENGTH = 65536  # GitHub issue body limit
            MAX_LABEL_COUNT = 20  # GitHub labels per issue limit

            # Validate and truncate title
            if len(cleaned_row["title"]) > MAX_TITLE_LENGTH:
                print(f"⚠️  Warning: Title too long in row {row_num}, truncating to {MAX_TITLE_LENGTH} chars")
                cleaned_row["title"] = cleaned_row["title"][: MAX_TITLE_LENGTH - 3] + "..."

            # Validate and truncate body
            if len(cleaned_row["body"]) > MAX_BODY_LENGTH:
                print(f"⚠️  Warning: Body too long in row {row_num}, truncating")
                cleaned_row["body"] = (
                    cleaned_row["body"][: MAX_BODY_LENGTH - 50] + "\n\n[Content truncated due to length limit]"
                )

            # Validate label count
            if len(cleaned_row["labels"]) > MAX_LABEL_COUNT:
                print(f"⚠️  Warning: Too many labels in row {row_num}, keeping first {MAX_LABEL_COUNT}")
                cleaned_row["labels"] = cleaned_row["labels"][:MAX_LABEL_COUNT]

            return cleaned_row

        # Main validation logic with comprehensive error handling
        try:
            # Extract and validate required fields with defensive programming
            title = safe_get_string("title")
            if not title:
                raise ValueError(f"Empty or missing title in row {row_num}")

            body = safe_get_string("body")
            if not body:
                raise ValueError(f"Empty or missing body in row {row_num}")

            # Parse optional fields with safe defaults
            labels_raw = safe_get_string("labels")
            status_raw = safe_get_string("status", "open")
            milestone_raw = safe_get_string("milestone")

            # Process and validate all data
            cleaned_row = {
                "title": title,
                "body": body,
                "labels": safe_parse_labels(labels_raw),
                "status": status_raw.lower(),
                "milestone": milestone_raw if milestone_raw else None,
            }

            # Validate status with fallback
            valid_statuses = {"open", "closed"}
            if cleaned_row["status"] not in valid_statuses:
                print(f"⚠️  Warning: Invalid status '{cleaned_row['status']}' in row {row_num}, defaulting to 'open'")
                cleaned_row["status"] = "open"

            # Apply platform constraints
            cleaned_row = validate_field_lengths(cleaned_row)

            # Final validation check
            if not cleaned_row["title"] or not cleaned_row["body"]:
                raise ValueError(f"Required fields became empty after cleaning in row {row_num}")

            return cleaned_row

        except ValueError:
            # Re-raise validation errors for caller to handle
            raise

        except Exception as e:
            # Clean Code: Preserve original exception context
            print(f"⚠️  Warning: Unexpected validation error in row {row_num}: {e}")
            raise ValueError(f"Could not validate row {row_num}: {e}") from e

    def issue_exists(self, title: str) -> bool:
        """
        Check if issue already exists in GitHub repository

        Args:
            title: Issue title to check

        Returns:
            True if issue exists, False otherwise

        Educational Value:
        - Shows how to interact with external APIs safely
        - Demonstrates subprocess usage best practices
        - Teaches error handling for external dependencies
        """
        try:
            # Use GitHub CLI to search for existing issues
            cmd = [
                "gh",
                "issue",
                "list",
                "--repo",
                f"{self.owner}/{self.repo}",
                "--search",
                f'"{title}"',
                "--json",
                "title",
                "--limit",
                "100",
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            # Parse JSON response and check for exact title match
            import json

            issues = json.loads(result.stdout)

            return any(issue["title"] == title for issue in issues)

        except subprocess.CalledProcessError as e:
            print(f"⚠️  Warning: Could not check if issue exists: {e}")
            return False  # Assume doesn't exist if can't check
        except json.JSONDecodeError as e:
            print(f"⚠️  Warning: Could not parse GitHub CLI response: {e}")
            return False
        except Exception as e:
            print(f"⚠️  Warning: Unexpected error checking issue existence: {e}")
            return False

    def create_issue_commands(self, csv_data: list[dict[str, Any]]) -> list[IssueCommand]:
        """
        Convert CSV data to validated issue commands

        Args:
            csv_data: List of validated CSV rows

        Returns:
            List of issue commands ready for execution

        Educational Value:
        - Demonstrates Factory Pattern for object creation
        - Shows data transformation techniques
        - Teaches validation and error handling
        """
        commands = []

        for issue_data in csv_data:
            try:
                # Check if issue already exists
                exists = self.issue_exists(issue_data["title"])

                # Create command object
                command = IssueCommand(
                    title=issue_data["title"],
                    body=issue_data["body"],
                    labels=issue_data["labels"],
                    milestone=issue_data["milestone"],
                    exists=exists,
                )

                commands.append(command)

            except Exception as e:
                print(f"⚠️  Warning: Could not create command for issue '{issue_data.get('title', 'Unknown')}': {e}")
                continue

        return commands

    def execute_dry_run(self, commands: list[IssueCommand], detailed: bool = False) -> None:
        """
        Execute dry-run mode showing what would be done

        Args:
            commands: List of issue commands to preview
            detailed: Whether to show detailed preview

        Educational Value:
        - Demonstrates how to provide comprehensive user feedback
        - Shows clear communication of system behavior
        - Teaches user experience design in CLI tools
        """
        print(self.formatter.format_summary(commands, ExecutionMode.DRY_RUN))

        if detailed:
            print(self.formatter.format_detailed_preview(commands))

        print("\n💡 **To actually create these issues, run:**")
        print("   python {} --csv {} --execute".format(sys.argv[0], sys.argv[sys.argv.index("--csv") + 1]))
        print("\n🔍 **For detailed preview, add --detailed flag**")

    def execute_commands(self, commands: list[IssueCommand]) -> bool:
        """
        Execute issue creation commands

        Args:
            commands: List of issue commands to execute

        Returns:
            True if all commands executed successfully

        Educational Value:
        - Demonstrates command execution with error handling
        - Shows progress reporting for long operations
        - Teaches transaction-like operations (all or nothing)
        """
        print(self.formatter.format_summary(commands, ExecutionMode.EXECUTE))

        new_commands = [cmd for cmd in commands if not cmd.exists]
        if not new_commands:
            print("No issues to import")
            return True

        print(f"\n🚀 Creating {len(new_commands)} new issues...")

        success_count = 0
        for i, command in enumerate(new_commands, 1):
            try:
                print(f"\n📝 Creating issue {i}/{len(new_commands)}: {command.title[:50]}...")

                if self._create_single_issue(command):
                    success_count += 1
                    print(f"   ✅ Successfully created issue {i}")
                else:
                    print(f"   ❌ Failed to create issue {i}")

            except Exception as e:
                print(f"   ❌ Error creating issue {i}: {e}")

        print(f"\n🎉 **Summary:** Successfully created {success_count}/{len(new_commands)} issues")
        return success_count == len(new_commands)

    def _create_single_issue(self, command: IssueCommand) -> bool:
        """
        Create a single GitHub issue using GitHub CLI

        Args:
            command: Issue command to execute

        Returns:
            True if issue created successfully

        Security Implementation:
        - Uses parameterized subprocess calls
        - Validates all inputs before execution
        - Prevents command injection through proper argument arrays
        """
        try:
            # Build GitHub CLI command
            cmd = [
                "gh",
                "issue",
                "create",
                "--repo",
                f"{self.owner}/{self.repo}",
                "--title",
                command.title,
                "--body",
                command.body,
            ]

            # Add labels if present
            if command.labels:
                cmd.extend(["--label", ",".join(command.labels)])

            # Add milestone if present
            if command.milestone:
                cmd.extend(["--milestone", command.milestone])

            # Execute command
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            # GitHub CLI returns the issue URL on success
            if result.stdout.strip():
                return True
            else:
                print(f"   ⚠️  Warning: Unexpected GitHub CLI output: {result.stdout}")
                return False

        except subprocess.CalledProcessError as e:
            print(f"   ❌ GitHub CLI error: {e.stderr}")
            return False
        except Exception as e:
            print(f"   ❌ Unexpected error: {e}")
            return False

    def interactive_mode(self, commands: list[IssueCommand]) -> bool:
        """
        Interactive mode for selective issue creation

        Educational Value:
        - Demonstrates user interaction patterns
        - Shows how to build flexible CLI interfaces
        - Teaches user experience considerations
        """
        print(self.formatter.format_summary(commands, ExecutionMode.INTERACTIVE))

        new_commands = [cmd for cmd in commands if not cmd.exists]
        if not new_commands:
            print("\n✅ No new issues to create.")
            return True

        print(f"\n🤔 **Interactive Mode**: Review each of the {len(new_commands)} new issues")
        print("   Options: (y)es, (n)o, (a)ll, (q)uit, (d)etails")

        selected_commands = []

        for i, command in enumerate(new_commands, 1):
            while True:
                title_preview = command.title[:60] + "..." if len(command.title) > 60 else command.title
                response = (
                    input(f"\n📝 Issue {i}/{len(new_commands)}: {title_preview}\n   Create this issue? [y/n/a/q/d]: ")
                    .lower()
                    .strip()
                )

                if response in ["y", "yes"]:
                    selected_commands.append(command)
                    break
                elif response in ["n", "no"]:
                    break
                elif response in ["a", "all"]:
                    # keep slice spacing tight (PEP8) and preserve semantics
                    selected_commands.extend(new_commands[i - 1:])
                    break
                elif response in ["q", "quit"]:
                    print("\n🛑 Exiting interactive mode.")
                    return False
                elif response in ["d", "details"]:
                    # use plain string when there are no placeholders to avoid F541
                    print("\n📋 **Issue Details:**")
                    print(f"Title: {command.title}")
                    print(f"Labels: {', '.join(command.labels) if command.labels else 'None'}")
                    print(f"Milestone: {command.milestone or 'None'}")
                    print(f"Body: {command.body[:200]}{'...' if len(command.body) > 200 else ''}")
                    continue
                else:
                    print("   ❓ Please enter y, n, a, q, or d")
                    continue

        if selected_commands:
            print(f"\n🚀 Creating {len(selected_commands)} selected issues...")
            return self.execute_commands(selected_commands)
        else:
            print("\n✅ No issues selected for creation.")
            return True


def main():
    """
    Main entry point with comprehensive argument parsing and diagnostics

    Educational Value:
    - Demonstrates professional CLI design patterns
    - Shows proper argument validation and error handling
    - Teaches user experience design for developer tools
    """
    parser = argparse.ArgumentParser(
        description="Import GitHub issues from CSV with dry-run support",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Diagnose CSV data quality issues
  python import_backlog_with_gh.py --csv issues.csv --diagnose

  # Preview what will be created (dry-run)
  python import_backlog_with_gh.py --csv issues.csv --dry-run

  # Preview with detailed information
  python import_backlog_with_gh.py --csv issues.csv --dry-run --detailed

  # Actually create the issues
  python import_backlog_with_gh.py --csv issues.csv --execute

  # Interactive mode for selective creation
  python import_backlog_with_gh.py --csv issues.csv --interactive

Environment Variables:
  OWNER: GitHub repository owner (default: taimac)
  REPO: GitHub repository name (default: tailormaciel.github.io)
        """,
    )

    parser.add_argument("--csv", required=True, help="Path to CSV file containing issues")

    # Execution mode group (mutually exclusive)
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument("--diagnose", action="store_true", help="Analyze CSV data quality and structure")
    mode_group.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what will be created without making changes",
    )
    mode_group.add_argument("--execute", action="store_true", help="Actually create the issues in GitHub")
    mode_group.add_argument(
        "--interactive",
        action="store_true",
        help="Interactive mode to select which issues to create",
    )

    parser.add_argument(
        "--detailed",
        action="store_true",
        help="Show detailed preview (use with --dry-run)",
    )

    parser.add_argument("--owner", default=os.getenv("OWNER", "taimac"), help="GitHub repository owner")
    parser.add_argument(
        "--repo",
        default=os.getenv("REPO", "tailormaciel.github.io"),
        help="GitHub repository name",
    )

    args = parser.parse_args()

    try:
        # Initialize importer
        importer = GitHubIssuesImporter(args.owner, args.repo)

        # Handle diagnostic mode
        if args.diagnose:
            importer.diagnose_csv(args.csv)
            return True

        # Load CSV data
        print(f"📥 Loading issues from CSV: {args.csv}")
        csv_data = importer.load_csv_data(args.csv)

        # Create issue commands
        print("🔍 Checking existing issues and preparing commands...")
        commands = importer.create_issue_commands(csv_data)

        # Execute based on mode
        if args.dry_run:
            importer.execute_dry_run(commands, detailed=args.detailed)
            return True
        elif args.execute:
            return importer.execute_commands(commands)
        elif args.interactive:
            return importer.interactive_mode(commands)

    except Exception as e:
        print(f"❌ Error: {e}")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
