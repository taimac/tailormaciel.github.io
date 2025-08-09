# Utils

This folder contains shared utility functions and helpers.

## Purpose

- Provides stateless, reusable functions for formatting, validation, etc.
- Supports all layers but should not contain business logic.

## OOP Principles

- **Single Responsibility**: Each utility does one thing well.
- **Reusability**: Utilities are designed to be used across components and services.

## Security Considerations

- Utilities that process user input should always sanitize and validate data.

## Testing Strategy

- Write unit tests for each utility function.
- Test edge cases and invalid inputs.

## Example

```js
// Example: sanitizeHtml utility
export function sanitizeHtml(input) {
    // Removes dangerous tags to prevent XSS
}
```

---