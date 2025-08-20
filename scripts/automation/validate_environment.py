#!/usr/bin/env python3
"""
Environment Validation Script

Architecture Notes:
- Implements Command Pattern for environment checks
- Uses Composite Pattern for aggregating validation results
- Demonstrates Defensive Programming principles

Security Considerations:
- Only executes read-only system commands
- Validates all external command outputs
- Fails safely when tools are missing

OOP Principles Applied:
- Single Responsibility: Each function validates one tool
- Open/Closed: Easy to add new validation checks
- Dependency Inversion: Uses abstractions for command execution

Educational Value:
- Shows how to build robust automation tools
- Demonstrates security-conscious system interaction
- Implements professional error handling patterns
"""

import os
import shlex
import subprocess
import sys

from packaging import version


class EnvironmentValidator:
    """
    Validates development environment setup

    Architecture Pattern: Command + Composite
    - Each validation is a command that can be executed independently
    - Results are composed into an overall environment health check

    Security Design:
    - Only executes whitelisted, read-only commands
    - Validates all external input before processing
    - Implements fail-safe defaults
    """

    def __init__(self):
        """
        Initialize validator with secure defaults

        Security Notes:
        - No external dependencies required for basic operation
        - All commands are hardcoded to prevent injection
        """
        self.checks_passed = 0
        self.checks_total = 0
        self.validation_results: list[tuple[str, bool, str]] = []

    def _parse_version(self, output: str) -> str | None:
        """
        Safely extract version number from command output

        Args:
            output: Raw command output string

        Returns:
            Version string if found, None otherwise

        Security Notes:
        - Defensive parsing prevents malformed output issues
        - Only extracts expected version patterns
        """
        # Defensive programming: handle malformed output gracefully
        if not output or not isinstance(output, str):
            return None

        # Look for version patterns (starts with digit)
        for token in output.split():
            if token and len(token) > 0 and token[0].isdigit():
                return token

        return None

    def _execute_safe_command(self, command: str) -> tuple[bool, str]:
        """
        Execute a system command safely with proper error handling

        Args:
            command: Command string to execute

        Returns:
            Tuple of (success, output)

        Security Implementation:
        - Uses shlex.split() to prevent shell injection
        - Captures both stdout and stderr safely
        - Implements timeout to prevent hanging
        """
        try:
            # Security: Use shlex.split to prevent shell injection
            result = subprocess.run(
                shlex.split(command),
                capture_output=True,
                text=True,
                timeout=10,  # Prevent hanging commands
            )

            # Get output from either stdout or stderr
            output = result.stdout.strip() or result.stderr.strip()

            return True, output

        except subprocess.TimeoutExpired:
            return False, f"Command timed out: {command}"
        except FileNotFoundError:
            return False, f"Command not found: {command.split()[0]}"
        except Exception as e:
            return False, f"Execution failed: {str(e)}"

    def validate_tool(
        self,
        command: str,
        min_version: str | None = None,
        tool_name: str | None = None,
    ) -> bool:
        """
        Validate a development tool is installed and meets version requirements

        Args:
            command: Shell command to check tool (e.g., 'python3 --version')
            min_version: Minimum required version as string (e.g., '3.8')
            tool_name: Human-readable tool name for reporting

        Returns:
            True if validation passes, False otherwise

        Architecture Notes:
        - Implements Template Method pattern for validation workflow
        - Uses Strategy pattern for different version checking approaches
        """
        self.checks_total += 1
        tool_name = tool_name or command.split()[0]

        # Execute command safely
        success, output = self._execute_safe_command(command)

        if not success:
            print(f"❌ {tool_name}: {output}")
            self.validation_results.append((tool_name, False, output))
            return False

        print(f"✅ {tool_name}: {output}")

        # Version validation if required
        if min_version:
            found_version = self._parse_version(output)

            if not found_version:
                error_msg = f"Could not parse version from output: {output}"
                print(f"⚠️  {tool_name}: {error_msg}")
                self.validation_results.append((tool_name, False, error_msg))
                return False

            try:
                if version.parse(found_version) < version.parse(min_version):
                    error_msg = f"Version {found_version} < required {min_version}"
                    print(f"❌ {tool_name}: {error_msg}")
                    self.validation_results.append((tool_name, False, error_msg))
                    return False
            except Exception as e:
                error_msg = f"Version comparison failed: {str(e)}"
                print(f"⚠️  {tool_name}: {error_msg}")
                self.validation_results.append((tool_name, False, error_msg))
                return False

        self.checks_passed += 1
        self.validation_results.append((tool_name, True, output))
        return True

    def run_all_validations(self) -> bool:
        """
        Execute all environment validations

        Returns:
            True if all validations pass, False otherwise

        Educational Notes:
        - Demonstrates how to build robust validation workflows
        - Shows proper error aggregation and reporting
        - Implements fail-fast vs. fail-safe decision making
        """
        print("🔍 Development Environment Validation")
        print("=" * 50)

        # Core development tools with minimum versions
        validations = [
            ("python3 --version", "3.8", "Python"),
            ("git --version", "2.30", "Git"),
            ("code --version", os.environ.get("VSCODE_MIN_VERSION", "1.80"), "VS Code"),
            ("python -m pip --version", None, "pip"),
            ("pytest --version", None, "pytest"),
        ]

        # Execute all validations (don't fail fast for better user experience)
        for command, min_version, tool_name in validations:
            self.validate_tool(command, min_version, tool_name)

        # Report results
        print("\n" + "=" * 50)
        print(f"📊 Validation Summary: {self.checks_passed}/{self.checks_total} checks passed")

        if self.checks_passed == self.checks_total:
            print("🎉 Environment is ready for development!")
            return True
        else:
            print("⚠️  Environment setup incomplete. Please install missing tools.")
            self._print_installation_guidance()
            return False

    def _print_installation_guidance(self):
        """
        Provide helpful installation guidance for failed checks

        Educational Notes:
        - Shows how to provide actionable error messages
        - Demonstrates user-friendly error reporting
        """
        print("\n🔧 Installation Guidance:")
        print("-" * 30)

        for tool_name, passed, _message in self.validation_results:
            if not passed:
                if "python" in tool_name.lower():
                    print(f"❌ {tool_name}: Version mismatch or not found")
                else:
                    print(f"❌ {tool_name}: Validation failed")


def main():
    """
    Main entry point for environment validation

    Architecture Notes:
    - Uses Facade pattern to provide simple interface
    - Implements proper exit codes for automation

    Security Notes:
    - No sensitive information exposed in output
    - Safe to run in any environment
    """
    validator = EnvironmentValidator()

    if validator.run_all_validations():
        sys.exit(0)  # Success
    else:
        sys.exit(1)  # Failure


if __name__ == "__main__":
    main()
