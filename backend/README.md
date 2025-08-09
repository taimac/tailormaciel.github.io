# Backend

This folder contains all server-side code for the personal website and knowledge base.

## Clean Architecture Mapping

- **controllers/**: Presentation Layer (handles HTTP requests/responses)
- **services/**: Application Layer (business logic/use cases)
- **models/**: Domain Layer (core entities and rules)
- **repositories/**: Infrastructure Layer (database/external services)
- **middleware/**: Cross-cutting concerns (auth, logging, etc.)
- **tests/**: Automated tests for backend code

## Learning Focus

- Demonstrates separation of concerns and dependency direction.
- Each subfolder maps to a Clean Architecture layer for clarity and maintainability.
