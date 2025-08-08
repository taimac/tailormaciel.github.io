"""
Environment validation script

Purpose:
    Ensures all required tools are installed and configured.
    Teaches automation, defensive programming, and repeatability.

Security:
    No secrets are checked in.
    Only public system info is displayed.

Clean Code:
    Single Responsibility - only validates environment.
    Defensive programming - robust version checks.
"""

import sys
import subprocess
from packaging import version  # Requires 'pip install packaging'

def parse_version(output):
    """
    Extracts the version number from a command output string.
    """
    for token in output.split():
        if token and token[0].isdigit():
            return token
    return None

def check(command, min_version=None):
    """
    Runs a shell command and checks if the version meets requirements.

    Args:
        command: The shell command to run (e.g., 'python3 --version')
        min_version: Minimum required version as a string (e.g., '3.8')

    Returns:
        True if check passes, False otherwise.

    Security Notes:
        - Only runs safe, read-only commands.
    """
    try:
        result = subprocess.run(shlex.split(command), capture_output=True, text=True)
        output = result.stdout.strip() or result.stderr.strip()
        print(f"{command}: {output}")
        if min_version:
            found_version = parse_version(output)
            if not found_version or version.parse(found_version) < version.parse(min_version):
                print(f"❌ {command} version must be >= {min_version}")
                return False
        return True
    except Exception as e:
        print(f"❌ {command} failed: {e}")
        return False

def main():
    print("== Environment Validation ==")
    checks = [
        check("python3 --version", "3.8"),
        check("git --version", "2.30"),
        check("code --version", "1.50"),
        check("which pip"),
    ]
    if all(checks):
        print("✅ Environment is ready!")
        sys.exit(0)
    else:
        print("❌ Environment setup incomplete.")
        sys.exit(1)

if __name__ == "__main__":
    main()