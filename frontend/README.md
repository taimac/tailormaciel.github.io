# Frontend

This folder contains all client-side code for the personal website and knowledge base system.

## Purpose

The frontend is responsible for presenting information to users, handling user interactions, and communicating with the backend API. It is organized to teach and demonstrate modern component-based architecture, OOP principles in JavaScript, and Clean Architecture mapping.

## Folder Structure

```
frontend/
├── js/
│   ├── components/   # UI Components (Presentation Layer)
│   ├── services/     # Business Logic (Application Layer)
│   └── utils/        # Utilities (Shared Helpers)
├── styles/           # CSS files (BEM methodology, responsive design)
└── assets/           # Static resources (images, fonts, etc.)
```

### js/components/

- **Purpose**: Contains reusable UI components (e.g., navigation, hero, note cards).
- **Architecture**: Follows the Presentation Layer of Clean Architecture.
- **OOP Concepts**: Each component is a class or function encapsulating its state and behavior.
- **Security**: Components must sanitize and encode any user-generated content before rendering to prevent XSS.

### js/services/

- **Purpose**: Contains business logic and API communication (e.g., fetching notes, authentication).
- **Architecture**: Maps to the Application Layer.
- **OOP Concepts**: Services encapsulate logic and can be tested independently.
- **Security**: All user input should be validated here before sending to backend.

### js/utils/

- **Purpose**: Shared utility functions (e.g., formatting, helpers).
- **Architecture**: Supports all layers, but should remain stateless and pure.

### styles/

- **Purpose**: CSS files organized using BEM methodology for maintainability.
- **Architecture**: Supports the Presentation Layer.
- **Performance**: Use CSS variables and responsive design for accessibility and speed.

### assets/

- **Purpose**: Static files (images, fonts, icons).
- **Best Practice**: Optimize assets for fast loading.

## Clean Architecture Mapping

- **Presentation Layer**: `js/components/`, `styles/`
- **Application Layer**: `js/services/`
- **Shared/Infrastructure**: `js/utils/`, `assets/`

## Security Notes

- Always validate and sanitize user input in services before processing.
- Encode output in components to prevent XSS.
- Never store sensitive data in frontend code.

## Testing

- Place frontend tests in a `tests/` folder at the same level as `js/` (or inside each subfolder).
- Use Jest or similar for JavaScript unit tests.
- See [../docs/](../docs/) for testing guides.

## Further Reading

- [docs/OOP_ARCHITECTURE_GUIDE.md](../docs/OOP_ARCHITECTURE_GUIDE.md)
- [docs/Daily_Development_Routine.md](../docs/Daily_Development_Routine.md)

---

*This README is designed to teach Clean Architecture, OOP, and security-first development in frontend engineering. For questions, see the documentation or ask: "Why is this folder organized this way?"*
