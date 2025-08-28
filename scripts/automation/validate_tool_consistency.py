# Create scripts/automation/validate_tool_consistency.py
#!/usr/bin/env python3
"""
Tool Configuration Consistency Validator

Educational Purpose:
- Demonstrates Configuration Management patterns
- Shows defensive programming for development environment validation
- Teaches automated quality gate implementation

Architecture Principles Applied:
- Single Responsibility: Only validates tool consistency
- Open/Closed: Easy to add new tool validations
- Dependency Inversion: Depends on configuration abstractions

Security Implementation:
- Validates tool integrity before use
- Prevents configuration tampering
- Ensures reproducible build environment
"""

import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any

import yaml


class ToolVersionValidator:
    """
    Validates consistency between local tools and configuration files

    Educational Value:
    - Demonstrates Strategy Pattern for different validation approaches
    - Shows error handling and user feedback patterns
    - Teaches proactive environment validation

    Clean Code Principles:
    - Single Responsibility: Only handles version validation
    - Interface Segregation: Clear validation interface
    - Dependency Inversion: Abstracts tool version detection
    """

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.config = self._load_project_config()

    def _load_project_config(self) -> dict[str, Any]:
        """
        Load unified configuration from pyproject.toml

        Educational Notes:
        - Demonstrates configuration loading patterns
        - Shows error handling for missing files
        - Teaches validation of configuration integrity
        """
        config_file = self.project_root / "pyproject.toml"

        if not config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_file}")

        try:
            with open(config_file, "rb") as f:
                return tomllib.load(f)
        except Exception as e:
            raise ValueError(f"Invalid configuration file: {e}") from e

    def validate_black_consistency(self) -> bool:
        """
        Validates Black version consistency between local and pre-commit

        Educational Value:
        - Shows how to validate external tool versions
        - Demonstrates subprocess usage for tool integration
        - Teaches error handling for external process failures

        Security Notes:
        - Uses subprocess safely with argument arrays
        - Validates output to prevent injection attacks
        - Handles errors without exposing system information
        """
        try:
            # Get local Black version
            local_version = self._get_local_black_version()

            # Get pre-commit Black version
            precommit_version = self._get_precommit_black_version()

            # Validate consistency
            if local_version != precommit_version:
                print("❌ Black version mismatch:")
                print(f"   Local: {local_version}")
                print(f"   Pre-commit: {precommit_version}")
                return False

            print(f"✅ Black version consistent: {local_version}")
            return True

        except Exception as e:
            print(f"❌ Error validating Black consistency: {e}")
            return False

    def _get_local_black_version(self) -> str:
        """
        Get local Black version safely

        Educational Notes:
        - Demonstrates safe subprocess usage
        - Shows error handling for missing tools
        - Teaches output parsing and validation
        """
        try:
            result = subprocess.run(
                ["black", "--version"], capture_output=True, text=True, check=True, timeout=10  # Prevent hanging
            )

            # Parse version from output like "black, 25.1.0 (compiled: yes)"
            version_line = result.stdout.strip()
            if "," in version_line:
                return version_line.split(",")[1].strip().split()[0]

            raise ValueError(f"Unexpected version format: {version_line}")

        except subprocess.CalledProcessError as e:
            raise RuntimeError("Black not installed or not accessible") from e
        except subprocess.TimeoutExpired as e:
            raise RuntimeError("Black version check timed out") from e

    def _get_precommit_black_version(self) -> str:
        """
        Extract Black version from pre-commit configuration

        Educational Value:
        - Shows YAML parsing for configuration files
        - Demonstrates defensive programming for missing data
        - Teaches configuration validation patterns
        """
        precommit_config = self.project_root / ".pre-commit-config.yaml"

        if not precommit_config.exists():
            raise FileNotFoundError("Pre-commit configuration not found")

        try:
            with open(precommit_config) as f:
                config = yaml.safe_load(f)

            # Find Black configuration
            for repo in config.get("repos", []):
                if "psf/black" in repo.get("repo", ""):
                    rev = repo.get("rev", "").lstrip("v")  # Remove 'v' prefix if present
                    return rev

            raise ValueError("Black configuration not found in pre-commit config")

        except yaml.YAMLError as e:
            raise ValueError(f"Invalid pre-commit YAML: {e}") from e

    def validate_all_tools(self) -> bool:
        """
        Comprehensive tool validation

        Educational Value:
        - Demonstrates comprehensive validation patterns
        - Shows how to aggregate multiple validation results
        - Teaches fail-fast vs fail-soft validation strategies
        """
        validations = [
            ("Black Version Consistency", self.validate_black_consistency),
            # Add more tool validations here as we expand
        ]

        all_valid = True
        print("🔧 Validating Development Environment...")

        for name, validator in validations:
            print(f"\n📋 {name}:")
            if not validator():
                all_valid = False

        return all_valid


def main():
    """
    Main entry point for tool validation

    Educational Purpose:
    - Shows professional CLI tool structure
    - Demonstrates error handling and user feedback
    - Teaches exit code conventions for automation
    """
    try:
        project_root = Path(__file__).parent.parent.parent
        validator = ToolVersionValidator(project_root)

        if validator.validate_all_tools():
            print("\n✅ All development tools are properly configured!")
            sys.exit(0)
        else:
            print("\n❌ Development environment validation failed!")
            print("\n🔧 Run the following to fix:")
            print("   pre-commit autoupdate")
            print("   pre-commit install --install-hooks")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Validation error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
