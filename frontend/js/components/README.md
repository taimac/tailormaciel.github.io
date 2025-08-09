# Components

This folder contains all reusable UI components for the frontend.

## Purpose

- Implements the **Presentation Layer** of Clean Architecture.
- Each component encapsulates its own state, rendering logic, and events.

## OOP Principles

- **Encapsulation**: Each component manages its own state and DOM logic.
- **Abstraction**: Components expose only necessary interfaces (e.g., props, events).
- **Reusability**: Components can be composed to build complex UIs.

## Security Considerations

- **Input Sanitization**: Always sanitize and encode any user-generated content before rendering to prevent XSS.
- **Principle of Least Privilege**: Components should not access global state directly.

## Testing Strategy

- Write unit tests for each component (e.g., with Jest or web-test-runner).
- Test rendering, event handling, and input sanitization.

## Example

```js
// Example: Navigation component
class Navigation {
    /**
     * Renders the navigation bar.
     * Security: Encodes all dynamic labels.
     */
    render() { /* ... */ }
}
```

---