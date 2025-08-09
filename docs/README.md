# Personal Website & Knowledge Base

A modern personal website with interconnected knowledge base, built with minimal frameworks to understand core programming principles. This project serves as a comprehensive learning platform for Object-Oriented Programming, Clean Architecture, and Security-First Development.

## 🎯 Educational Mission

This isn't just a website—it's a **hands-on software engineering education**. Every component demonstrates fundamental programming concepts while building a production-quality application.

### Learning Objectives
- **Master OOP Principles**: Encapsulation, Inheritance, Polymorphism, Abstraction through practical application
- **Understand Clean Architecture**: Clear separation of concerns across presentation, application, domain, and infrastructure layers  
- **Apply Security-First Development**: Implement SDD principles from foundation up, not as an afterthought
- **Practice Professional Workflows**: Git branching, TDD, code review, and documentation-driven development

## ✨ Features

- 🎨 **Modern, responsive design** inspired by shawhintalebi.com
- 📚 **Interconnected knowledge base** for CS studies with graph-like connections
- 🔐 **Secure authentication system** for private documents and notes
- 🔗 **Dynamic content linking** with intelligent cross-references
- 📱 **Mobile-first responsive design** with progressive enhancement
- 🧪 **Comprehensive testing** with 70%+ coverage requirement
- 🏗️ **Component-based architecture** demonstrating modern software patterns

## 🏛️ Architecture

### Technology Stack (Minimal by Design)
- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+) - *No frameworks to understand fundamentals*
- **Backend**: Python with Flask - *Minimal framework to see HTTP/web concepts clearly*
- **Database**: SQLite → PostgreSQL progression - *Start simple, add complexity as understanding grows*
- **Authentication**: Custom JWT implementation - *Learn security concepts from ground up*
- **Testing**: pytest for backend, vanilla JS testing for frontend
- **Build**: Minimal tooling - *Focus on understanding, not configuration*

### Clean Architecture Layers
```
🎨 Presentation Layer
├── Frontend Components (Modal, Navigation, Card)
├── HTTP Controllers (API endpoints)
└── Input Validation & Output Formatting

🔧 Application Layer (Use Cases)
├── AuthService (Login, registration, session management)
├── ContentService (CRUD operations, business workflows)
├── KnowledgeService (Graph connections, search algorithms)
└── SecurityService (Validation, authorization, audit)

🧠 Domain Layer (Business Rules)
├── Entities (User, Note, Project, ContentItem)
├── Value Objects (Email, Password, Tag)
├── Business Rules (Access control, content policies)
└── Domain Events (User actions, content changes)

🗄️ Infrastructure Layer
├── Database (Repository pattern, connection management)
├── File System (Document storage, uploads)
├── External Services (Future: OAuth, APIs)
└── Security (Encryption, hashing, secure storage)
```

## 📁 Project Structure

```
personal-website/
├── 📋 docs/                          # Documentation-driven development
│   ├── Daily_Development_Routine.md  # Complete workflow guide
│   ├── OOP_ARCHITECTURE_GUIDE.md     # Architectural decisions & patterns
│   ├── SETUP.md                      # Development environment setup
│   ├── backlog.md                    # Auto-updated from GitHub Issues
│   └── learning_progress.md          # Educational milestone tracking
│
├── 🎨 frontend/                      # Client-side application
│   ├── index.html                    # Semantic HTML foundation
│   ├── styles/                       # CSS Architecture (BEM methodology)
│   │   ├── main.css                  # Global styles, CSS custom properties
│   │   ├── components.css            # Component-specific styles
│   │   └── responsive.css            # Mobile-first responsive breakpoints
│   ├── js/                           # Modular JavaScript (ES6+ classes)
│   │   ├── components/               # UI Components demonstrating OOP
│   │   │   ├── Navigation.js         # Encapsulated navigation logic
│   │   │   ├── Modal.js              # Base modal class (inheritance demo)
│   │   │   ├── Card.js               # Polymorphic content rendering
│   │   │   └── SecureForm.js         # Input validation & XSS prevention
│   │   ├── services/                 # Business Logic Services
│   │   │   ├── AuthService.js        # Authentication abstraction
│   │   │   ├── ContentService.js     # Content management API layer
│   │   │   ├── SecurityService.js    # Client-side security utilities
│   │   │   └── EventBus.js           # Observer pattern implementation
│   │   └── main.js                   # Application bootstrap & orchestration
│   └── assets/                       # Static resources
│
├── ⚙️ backend/                       # Server-side application
│   ├── app.py                        # Application factory pattern
│   ├── config.py                     # Environment-based configuration
│   ├── models/                       # Domain Layer (Entities)
│   │   ├── base.py                   # Abstract base model with common behavior
│   │   ├── user.py                   # User entity with authentication logic
│   │   ├── content.py                # Content base class for inheritance
│   │   ├── knowledge_item.py         # Knowledge base entity
│   │   └── project.py                # Project portfolio entity
│   ├── services/                     # Application Layer (Use Cases)
│   │   ├── auth_service.py           # Authentication & authorization logic
│   │   ├── content_service.py        # Content management business rules
│   │   ├── knowledge_service.py      # Knowledge graph operations
│   │   └── security_service.py       # Security validation & enforcement
│   ├── controllers/                  # Presentation Layer (HTTP handlers)
│   │   ├── auth_controller.py        # Authentication endpoints
│   │   ├── content_controller.py     # Content CRUD API
│   │   └── knowledge_controller.py   # Knowledge base API
│   ├── repositories/                 # Infrastructure Layer (Data access)
│   │   ├── base_repository.py        # Abstract repository pattern
│   │   ├── user_repository.py        # User data access
│   │   └── content_repository.py     # Content data access
│   ├── middleware/                   # Cross-cutting concerns
│   │   ├── auth_middleware.py        # JWT token validation
│   │   ├── security_middleware.py    # CORS, rate limiting, security headers
│   │   └── logging_middleware.py     # Request/response logging
│   └── tests/                        # Comprehensive test suite
│       ├── unit/                     # Unit tests for individual classes
│       ├── integration/              # Integration tests across layers
│       └── fixtures/                 # Test data and mocks
│
├── 📝 scripts/                       # Development utilities
│   ├── init_database.py              # Database setup with sample data
│   ├── run_tests.py                  # Test runner with coverage reporting
│   ├── fetch_github_project_backlog.py # Sync GitHub Issues to local backlog
│   └── learning_progress_tracker.py  # Track educational milestones
│
└── 📋 Configuration Files
    ├── requirements.txt               # Python dependencies
    ├── pytest.ini                    # Test configuration
    ├── .gitignore                     # Git ignore patterns
    └── README.md                      # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ (with pip and venv)
- Git for version control
- VSCode with GitHub Copilot (recommended)

### Setup Development Environment
```bash
# 1. Clone repository
git clone <your-repo-url>
cd personal-website

# 2. Set up backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Initialize database
python scripts/init_database.py

# 4. Start backend server
python app.py
# Backend available at: http://127.0.0.1:5000

# 5. Start frontend (new terminal)
cd ../frontend
python -m http.server 3000
# Frontend available at: http://localhost:3000
```

### Verify Installation
```bash
# Run tests to ensure everything works
cd backend
python -m pytest tests/ -v
# All tests should pass

# Check code quality
python -m flake8 . --max-line-length=88
# Should have minimal warnings
```

## 💻 Development Philosophy

### Educational Approach
- **Learn by Building**: Every feature teaches fundamental concepts
- **Minimal Frameworks**: Understand what libraries actually do for you
- **Security-First**: Build security awareness into development process
- **Test-Driven**: Write tests first to drive better design
- **Documentation-Driven**: Document architectural decisions for learning

### Code Quality Standards
- **OOP Principles**: Every class demonstrates encapsulation, clear responsibilities
- **Clean Architecture**: Dependencies point inward, layers are clearly separated
- **Security Validation**: All inputs validated, outputs encoded, authentication required
- **Comprehensive Testing**: 70%+ test coverage with meaningful tests
- **Clear Documentation**: Every method explains purpose, security considerations, and design decisions

### Workflow Requirements
- **Feature Branches**: `feature/issue-N-description` format
- **TDD Cycle**: Red (failing test) → Green (minimal implementation) → Refactor
- **Daily Learning Log**: Document OOP concepts applied and security measures implemented
- **Code Review Checklist**: Manual review for OOP principles, security, and clean code

## 🎓 Learning Progression

### Phase 1: OOP Fundamentals ✅
- [x] Basic class structure and encapsulation
- [x] Inheritance vs composition understanding
- [x] Polymorphism with card components
- [x] Abstraction through service layers

### Phase 2: Clean Architecture 🚧
- [ ] Layer separation implementation
- [ ] Dependency injection setup
- [ ] Repository pattern for data access
- [ ] Service layer with business logic

### Phase 3: Security Implementation 📋
- [ ] Authentication system with JWT
- [ ] Input validation and sanitization
- [ ] Authorization and access control
- [ ] Security audit and testing

### Phase 4: Advanced Patterns 📋
- [ ] Observer pattern for events
- [ ] Factory pattern for component creation
- [ ] Strategy pattern for algorithms
- [ ] Command pattern for user actions

## 🔐 Security Features

- **Input Validation**: All user inputs validated and sanitized at boundaries
- **Authentication**: JWT-based authentication with secure token handling
- **Authorization**: Role-based access control for private content
- **Password Security**: Bcrypt hashing, never plain text storage
- **XSS Prevention**: Output encoding and Content Security Policy
- **SQL Injection Prevention**: Parameterized queries, no string concatenation
- **Rate Limiting**: Prevent brute force attacks on authentication
- **Secure Headers**: HTTPS enforcement, secure cookies, HSTS

## 🧪 Testing Strategy

### Test Categories
- **Unit Tests**: Individual class and method testing
- **Integration Tests**: Service layer and database interaction testing
- **Security Tests**: Validation of security measures and vulnerability prevention
- **Frontend Tests**: Component behavior and user interaction testing

### Coverage Requirements
- Minimum 70% code coverage across all layers
- 100% coverage for security-critical functions
- All public methods must have corresponding tests
- Error handling paths must be tested

## # Documentation

Project documentation, architectural decisions, and learning records.

- **ADR**: Architectural Decision Records
- **Setup guides**: Environment and workflow
- **Backlog**: Project planning and progress

**Learning:**  
Highlights the importance of documentation-driven development and knowledge sharing.

## 🤝 Contributing

This is primarily an educational project. Contributions should:
- Follow established OOP patterns and clean architecture principles
- Include comprehensive tests and security considerations
- Document learning objectives and architectural decisions
- Maintain focus on understanding core concepts over using advanced tools

### Development Workflow
1. Review `docs/Daily_Development_Routine.md` for complete process
2. Create feature branch following naming convention
3. Write failing tests first (TDD approach)
4. Implement minimal code to pass tests
5. Refactor for clean code and security
6. Document learning outcomes and architectural decisions

## 📄 License

This project is for educational purposes. Feel free to use as a learning resource or foundation for your own educational projects.

---

**Remember**: The goal isn't just to build a website, but to master Object-Oriented Programming, Clean Architecture, and Security principles through hands-on application. Every line of code should teach or demonstrate a fundamental software engineering concept.