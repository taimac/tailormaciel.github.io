"""
Utility Functions for Script Operations

Security Focus:
- All utilities implement secure defaults
- Input validation on all public interfaces
- No sensitive data exposure in logging
"""

from .http_session import create_session_with_pooling_and_timeout

__all__ = ["create_session_with_pooling_and_timeout"]
