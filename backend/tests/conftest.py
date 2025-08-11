import sys
import os
import pytest

# Ensure backend package is on path before imports

from backend.app import create_app  # noqa: E402

@pytest.fixture
def client():
    app = create_app('development')
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c