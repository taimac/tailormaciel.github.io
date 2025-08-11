# 📋 Daily Development Routine - Complete Workflow Guide

## 🎯 Purpose

This document defines the **complete daily workflow** for developing your personal website project. Every development session should follow this routine to build professional habits and ensure code quality.

**Target Audience**: Junior developers learning professional development practices.

---

## 🌅 Morning Setup Routine (Every Development Session)

### **1. Terminal & Environment Setup**

#### **Open Terminal and Navigate**
```bash
# 1. Open terminal (Windows: PowerShell, Mac/Linux: Terminal)
cd /path/to/your/personal-website

# Verify you're in the right place
ls -la
# Should see: backend/, frontend/, docs/, README.md, .git/

# 2. Check Git status first thing
git status
# This tells you:
# - Which branch you're on
# - Any uncommitted changes
# - If you need to pull updates
```

#### **Activate Virtual Environment**
```bash
# Navigate to backend directory
cd backend

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Verify activation - you should see (venv) in your prompt
which python  # Should point to venv/bin/python

# Check installed dependencies
pip list
```

**Why this matters:**
- **Isolation**: Prevents conflicts with system Python packages
- **Consistency**: Same environment every time
- **Learning**: Understand dependency management

---

### **2. Project Status Check**

#### **Update from Remote Repository**
```bash
# Check for remote changes
git fetch origin

# See what's different
git status

# If behind, pull changes
git pull origin dev  # Assuming dev is your main development branch

# If there are merge conflicts, resolve them now
```

#### **Review Current State**
```bash
# Check what you were working on last
git log --oneline -10  # See last 10 commits

# Check current branch
git branch -a  # See all branches

# Review your backlog
cat docs/backlog.md | head -20  # See current priorities
```

---

### **3. Development Environment Validation**

#### **Backend Health Check**
```bash
# From backend/ directory with venv activated

# 1. Run tests to ensure nothing is broken
python -m pytest tests/ -v
# All tests should pass before starting new work

# 2. Check code quality
python -m flake8 . --count --max-line-length=88
# Should have minimal warnings

# 3. Start backend server
python app.py
# Should start without errors on http://127.0.0.1:5000
```

#### **Frontend Health Check**
```bash
# Open second terminal window/tab
cd /path/to/your/personal-website/frontend

# Start frontend server
python -m http.server 3000
# Should serve on http://localhost:3000

# Quick browser test
# Open http://localhost:3000 - verify page loads
```

**Learning Points:**
- **Testing First**: Always verify working state before changes
- **Multiple Terminals**: Learn to manage multiple processes
- **Health Checks**: Prevent working on broken foundation

---

## 💻 Feature Development Workflow

### **4. Feature Planning & Branch Creation**

#### **Choose Your Task**
```bash
# 1. Review current priorities
cat docs/backlog.md

# 2. Check GitHub Issues (if using)
# Visit your repository's Issues tab
# Choose an issue to work on

# 3. Update local backlog
python scripts/fetch_github_project_backlog.py  # If you have this script
git add docs/backlog.md
git commit -m "Update backlog for today's work"
```

#### **Create Feature Branch**
```bash
# From dev branch, create feature branch
git checkout dev
git pull origin dev  # Ensure you have latest

# Create feature branch with descriptive name
git checkout -b feature/issue-5-add-user-authentication
# Format: feature/issue-N-brief-description

# Push branch to remote
git push -u origin feature/issue-5-add-user-authentication
```

**Branch Naming Convention:**
- `feature/issue-N-description` - New features
- `bugfix/issue-N-description` - Bug fixes
- `refactor/component-name` - Code improvements
- `docs/update-setup-guide` - Documentation updates

---

### **5. Test-Driven Development Cycle**

#### **Write Tests First (TDD Approach)**
```bash
# 1. Create test file for your feature
touch tests/test_user_authentication.py

# 2. Write failing test first
```

```python
# tests/test_user_authentication.py
import pytest
from backend.services.auth_service import AuthService

class TestUserAuthentication:
    def test_user_can_register_with_valid_data(self):
        # Arrange
        auth_service = AuthService()
        user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'SecurePass123!'
        }
        
        # Act
        result = auth_service.register_user(user_data)
        
        # Assert
        assert result.success == True
        assert result.user_id is not None
        assert 'password' not in result.user_data  # Security: no password in response
```

#### **Run Tests (Should Fail)**
```bash
# Run the specific test
python -m pytest tests/test_user_authentication.py::TestUserAuthentication::test_user_can_register_with_valid_data -v

# Expected: Test should fail because AuthService.register_user() doesn't exist yet
```

#### **Implement Minimum Code to Pass Test**
```python
# backend/services/auth_service.py
from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class RegistrationResult:
    success: bool
    user_id: str = None
    user_data: Dict[str, Any] = None
    error_message: str = None

class AuthService:
    def register_user(self, user_data: Dict[str, Any]) -> RegistrationResult:
        # Minimum implementation to pass test
        # TODO: Add real validation, password hashing, database storage
        
        # Basic validation
        if not user_data.get('username'):
            return RegistrationResult(success=False, error_message="Username required")
        
        # Mock success for now
        return RegistrationResult(
            success=True,
            user_id="user_123",
            user_data={
                'username': user_data['username'],
                'email': user_data['email']
                # Note: password deliberately excluded for security
            }
        )
```

#### **Run Tests Again (Should Pass)**
```bash
python -m pytest tests/test_user_authentication.py -v
# Should pass now

# Run all tests to ensure nothing broke
python -m pytest tests/ -v
```

---

### **6. Code Quality, Automation & Documentation**

#### **Automated Code Quality Enforcement (Pre-commit Hook)**

**Why Use a Pre-commit Hook?**
- **Automation**: Ensures every commit meets code quality standards automatically.
- **Security**: Prevents accidental inclusion of risky or low-quality code.
- **Professional Workflow**: Mirrors industry practices and reinforces clean code habits.

**How It Works:**
A pre-commit hook is installed at `.git/hooks/pre-commit` and runs automatically before every commit.  
It performs the following actions:
1. **Removes unused imports and variables** (`autoflake`)
2. **Auto-formats code** (`autopep8` or `black`)
3. **Removes trailing whitespace** (via `sed`)
4. **Runs linting checks** (`flake8`)
5. **Blocks the commit if any issues remain**

**Required Tools:**
```bash
pip install autoflake autopep8 flake8
# or, if using black:
pip install black
```

**Testing the Pre-commit Hook:**
1. Make a code style error (e.g., add an unused import or trailing whitespace).
2. Try to commit:
    ```bash
    git add .
    git commit -m "test: check pre-commit hook"
    ```
3. Observe:
   - If issues exist, the commit is blocked and errors are shown.
   - If all checks pass, the commit proceeds.

**Troubleshooting:**
- If your commit is blocked, read the error messages and fix the issues.
- If the hook does not run, ensure it is executable:
    ```bash
    chmod +x .git/hooks/pre-commit
    ```
- For advanced configuration, see `.flake8` and the pre-commit script.

---

#### **Add Comprehensive Documentation**
```python
class AuthService:
    """
    Handles user authentication and authorization
    
    Security Principles Applied:
    - Passwords are hashed, never stored in plain text
    - Input validation prevents injection attacks
    - Rate limiting prevents brute force attacks
    
    OOP Principles Demonstrated:
    - Encapsulation: Auth logic contained in one class
    - Single Responsibility: Only handles authentication
    - Dependency Injection: Uses repository pattern for data access
    """
    
    def __init__(self, user_repository: UserRepository, password_hasher: PasswordHasher):
        """
        Initialize auth service with dependencies
        
        Args:
            user_repository: Data access layer for user operations
            password_hasher: Service for secure password operations
            
        Architecture Note:
            Dependencies injected to support testing and flexibility
            Follows Clean Architecture dependency inversion principle
        """
        self._user_repository = user_repository
        self._password_hasher = password_hasher
        self._failed_attempts = {}  # In-memory for demo, use Redis in production
    
    def register_user(self, user_data: Dict[str, Any]) -> RegistrationResult:
        """
        Register a new user with security validation
        
        Args:
            user_data: Dictionary containing username, email, password
            
        Returns:
            RegistrationResult with success status and user info
            
        Raises:
            ValidationError: If input data is invalid
            SecurityError: If data contains potential threats
            
        Security Measures:
        - Input validation and sanitization
        - Password strength requirements
        - Email format validation
        - Username uniqueness check
        - SQL injection prevention through parameterized queries
        
        Business Rules:
        - Username must be 3-30 characters, alphanumeric + underscore
        - Email must be valid format and unique
        - Password must meet complexity requirements
        """
        # Implementation here...
```

---

#### **Manual Code Review Checklist**
```bash
# Before committing, manually check:

# 1. OOP Principles
echo "OOP Review:"
echo "- Does each class have single responsibility?"
echo "- Are private methods/data properly encapsulated?"
echo "- Is inheritance used appropriately (IS-A relationship)?"
echo "- Would composition be better than inheritance?"

# 2. Security Review
echo "Security Review:"
echo "- Is user input validated and sanitized?"
echo "- Are passwords hashed, never plain text?"
echo "- Are SQL queries parameterized?"
echo "- Do error messages avoid revealing system details?"

# 3. Clean Code Review
echo "Clean Code Review:"
echo "- Are names descriptive and meaningful?"
echo "- Are functions small and focused?"
echo "- Is code self-documenting?"
echo "- Are magic numbers replaced with constants?"

# 4. Architecture Review
echo "Architecture Review:"
echo "- Is business logic in service layer?"
echo "- Are controllers thin (only HTTP handling)?"
echo "- Are dependencies pointing inward?"
echo "- Is the code testable?"
```

---

### **7. Commit & Documentation Process**

#### **Stage and Commit Changes**
```bash
# 1. Review what you're about to commit
git diff  # See all changes
git status  # See files to be committed

# 2. Add files strategically (not all at once)
git add tests/test_user_authentication.py
git add backend/services/auth_service.py

# 3. Commit with descriptive message
git commit -m "feat: Add user registration with security validation

- Implement AuthService.register_user() method
- Add comprehensive input validation
- Include password strength requirements
- Add tests for registration flow
- Follow TDD approach with failing test first

Security features:
- Password hashing (never plain text storage)
- Input sanitization prevents injection
- Username uniqueness validation

Architecture:
- Service layer contains business logic
- Dependency injection for testability
- Repository pattern for data access

Closes #5"
```

**Commit Message Format:**
```
type: Brief description (50 chars max)

Detailed explanation of what and why (wrap at 72 chars)

- Bullet points for key changes
- Security considerations
- Architecture decisions
- Learning objectives met

Closes #issue-number
```

#### **Update Documentation**
```bash
# Update relevant documentation
echo "## User Authentication Added" >> docs/CHANGELOG.md
echo "- Added AuthService with registration functionality" >> docs/CHANGELOG.md
echo "- Implemented security validation and password hashing" >> docs/CHANGELOG.md

# Update learning progress
echo "✅ Phase 2: Authentication service implemented" >> docs/learning_progress.md

# Commit documentation updates
git add docs/
git commit -m "docs: Update changelog and learning progress"
```

---

## 🔄 Mid-Day Check-in Routine

### **8. Progress Review (Every 2-3 Hours)**

#### **Save Work in Progress**
```bash
# Even if not complete, save your progress
git add .
git commit -m "WIP: User authentication - partial implementation

- Added basic validation logic
- Still TODO: password hashing integration
- Tests passing for current implementation"

git push origin feature/issue-5-add-user-authentication
```

#### **Run Full Test Suite**
```bash
# Ensure you haven't broken anything
python -m pytest tests/ -v --tb=short

# Check test coverage
python -m pytest tests/ --cov=backend --cov-report=term-missing

# Target: Keep coverage above 70%
```

#### **Code Quality Check**
```bash
# Manual checks are now automated by the pre-commit hook!
# You can still run these manually if needed:
python -m flake8 backend/ --count --statistics
python -m pylint backend/ --score=y
python -m black backend/
```

---

### **9. Learning Reflection**

#### **Document What You Learned**
```bash
# Create daily learning log
echo "## $(date +%Y-%m-%d) - Learning Log" >> docs/daily_learning.md
echo "" >> docs/daily_learning.md
echo "### What I Implemented:" >> docs/daily_learning.md
echo "- User registration service with AuthService class" >> docs/daily_learning.md
echo "" >> docs/daily_learning.md
echo "### OOP Concepts Applied:" >> docs/daily_learning.md
echo "- Encapsulation: AuthService contains all auth logic" >> docs/daily_learning.md
echo "- Single Responsibility: Service only handles authentication" >> docs/daily_learning.md
echo "" >> docs/daily_learning.md
echo "### Security Concepts Learned:" >> docs/daily_learning.md
echo "- Password hashing prevents plain text storage" >> docs/daily_learning.md
echo "- Input validation prevents injection attacks" >> docs/daily_learning.md
echo "" >> docs/daily_learning.md
echo "### Questions/Challenges:" >> docs/daily_learning.md
echo "- How to implement rate limiting for login attempts?" >> docs/daily_learning.md
echo "- Best practices for JWT token expiration?" >> docs/daily_learning.md
```

---

## 🌅 End-of-Day Routine

### **10. Wrap-up and Planning**

#### **Final Commit and Push**
```bash
# Ensure all work is committed
git status  # Should be clean

# Push to remote
git push origin feature/issue-5-add-user-authentication

# Update main development branch with latest
git checkout dev
git pull origin dev
```

#### **Update Project Status**
```bash
# Update backlog with progress
echo "✅ Issue #5: User registration - COMPLETED" >> docs/backlog.md
echo "🚧 Issue #6: User login - IN PROGRESS" >> docs/backlog.md

# Plan tomorrow's work
echo "## Tomorrow's Priorities:" >> docs/daily_learning.md
echo "1. Implement user login functionality" >> docs/daily_learning.md
echo "2. Add password reset feature" >> docs/daily_learning.md
echo "3. Create login modal component" >> docs/daily_learning.md

# Commit documentation updates
git add docs/
git commit -m "docs: End of day progress update"
git push origin dev
```

#### **Environment Cleanup**
```bash
# Stop development servers
# Press Ctrl+C in terminals running:
# - Backend server (python app.py)
# - Frontend server (python -m http.server)

# Deactivate virtual environment
deactivate

# Close terminals or leave open for tomorrow
```

---

## 🔥 Emergency Procedures

### **When Things Go Wrong**

#### **Git Issues**
```bash
# Accidentally committed to wrong branch
git log --oneline -5  # Find the commit
git reset --hard HEAD~1  # Undo last commit (keeps changes in working directory)
git checkout correct-branch
git add .
git commit -m "Your commit message"

# Merge conflicts
git status  # See conflicted files
# Edit files to resolve conflicts (look for <<<<<<< ======= >>>>>>>)
git add resolved-file.py
git commit -m "Resolve merge conflict in resolved-file.py"

# Lost work (committed but can't find)
git reflog  # Shows all recent Git actions
git checkout commit-hash  # Recover lost commit
```

#### **Virtual Environment Issues**
```bash
# Environment corrupted
rm -rf venv/  # Delete old environment
python -m venv venv  # Create new one
source venv/bin/activate  # Activate
pip install -r requirements.txt  # Reinstall dependencies

# Python path issues
which python  # Should point to venv
pip list  # Should show your project dependencies
```

#### **Server Won't Start**
```bash
# Port already in use
lsof -ti:5000 | xargs kill -9  # Kill process on port 5000
lsof -ti:3000 | xargs kill -9  # Kill process on port 3000

# Module import errors
export PYTHONPATH="${PYTHONPATH}:$(pwd)"  # Add current directory to Python path
python -c "import sys; print('\n'.join(sys.path))"  # Debug Python path
```

---

## 📚 Learning Objectives Checklist

### **Daily Learning Goals**
Each development session should advance these objectives:

#### **Technical Skills**
- [ ] **Git Workflow**: Proper branching, committing, and merging
- [ ] **Testing**: Write tests before implementation (TDD)
- [ ] **Code Quality**: Follow clean code principles
- [ ] **Documentation**: Document decisions and learning

#### **OOP Understanding**
- [ ] **Identify Patterns**: Recognize which OOP principles apply
- [ ] **Design Decisions**: Choose between inheritance vs composition
- [ ] **Encapsulation**: Properly hide implementation details
- [ ] **Polymorphism**: Use common interfaces with different implementations

#### **Security Awareness**
- [ ] **Input Validation**: Sanitize all user inputs
- [ ] **Authentication**: Secure login/logout processes
- [ ] **Authorization**: Control access to resources
- [ ] **Data Protection**: Hash passwords, encrypt sensitive data

#### **Architecture Knowledge**
- [ ] **Layer Separation**: Keep concerns properly separated
- [ ] **Service Design**: Create focused, single-responsibility services
- [ ] **Dependency Management**: Use injection and inversion principles
- [ ] **Testing Strategy**: Make code testable through good design

---

## 🎯 Weekly Review Process

### **Every Friday - Week Retrospective**

#### **Technical Progress Review**
```bash
# Generate weekly report
echo "# Week of $(date +%Y-%m-%d) - Development Summary" > weekly_report.md
echo "" >> weekly_report.md

# Count commits this week
git log --since="1 week ago" --oneline | wc -l
echo "Commits this week: $(git log --since='1 week ago' --oneline | wc -l)" >> weekly_report.md

# List completed features
git log --since="1 week ago" --grep="feat:" --oneline >> weekly_report.md

# Run test coverage report
python -m pytest tests/ --cov=backend --cov-report=term-missing | tail -1 >> weekly_report.md
```

#### **Learning Assessment**
```markdown
## Questions to Answer Each Week:
1. What OOP principle did I apply most this week?
2. What security vulnerability did I learn to prevent?
3. What design pattern did I implement and why?
4. What would I do differently next week?
5. What concepts do I need to study more?
```

---

## 💡 Tips for Success

### **Habits to Build**
1. **Always start with tests** - TDD forces better design
2. **Commit small, commit often** - Makes debugging easier
3. **Document your thinking** - Helps future you understand decisions
4. **Review code before committing** - Catch issues early
5. **Keep learning log** - Track progress and identify gaps

### **Common Mistakes to Avoid**
1. **Skipping tests** - "I'll add them later" never happens
2. **Large commits** - Hard to review and debug
3. **Working on main/dev directly** - Always use feature branches
4. **Ignoring error messages** - Read and understand every error
5. **Copy-pasting code** - Understand what you're adding

### **When You're Stuck**
1. **Read error messages carefully** - They usually tell you what's wrong
2. **Check documentation** - Look at your own docs first
3. **Write a test** - Often clarifies what you're trying to achieve
4. **Break problem down** - Make the smallest possible change
5. **Take a break** - Sometimes the solution comes when you step away

---

## 🛠️ Pre-commit Hook Reference

```bash
# .git/hooks/pre-commit (must be executable)
autoflake --in-place --remove-unused-variables --remove-all-unused-imports -r backend scripts
autopep8 --in-place --recursive backend scripts
# black backend scripts
find backend scripts -name "*.py" -exec sed -i 's/[ \t]*$//' {} +
flake8 backend scripts
```