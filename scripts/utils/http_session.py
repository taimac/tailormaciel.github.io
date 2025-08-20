import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

DEFAULT_TIMEOUT = 30  # Default timeout in seconds


def create_session_with_pooling_and_timeout(
    pool_connections=10,
    pool_maxsize=100,
    retries=3,
    backoff_factor=0.5,
    timeout=DEFAULT_TIMEOUT,
):
    """
    Creates a requests.Session with connection pooling, retries, and default timeout.

    Args:
        pool_connections (int): Number of connection pools.
        pool_maxsize (int): Maximum number of connections in the pool.
        retries (int): Number of retries for transient errors.
        backoff_factor (float): Backoff factor for retries.
        timeout (int): Default timeout for requests.

    Returns:
        requests.Session: Configured session object.
    """
    session = requests.Session()

    # Configure retries for transient errors
    retry_strategy = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=[429, 500, 502, 503, 504],  # Retry on these HTTP status codes
        allowed_methods=["HEAD", "GET", "OPTIONS"],  # Retry only safe methods
    )

    # Configure HTTPAdapter with connection pooling
    adapter = HTTPAdapter(
        pool_connections=pool_connections,
        pool_maxsize=pool_maxsize,
        max_retries=retry_strategy,
    )
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    # Add a default timeout to all requests
    session.request = _add_default_timeout(session.request, timeout)

    return session


def _add_default_timeout(request_method, timeout):
    """
    Wraps a request method to add a default timeout if not provided.

    Args:
        request_method (callable): The original request method.
        timeout (int): Default timeout to apply.

    Returns:
        callable: Wrapped request method with default timeout.
    """

    def wrapped_request(*args, **kwargs):
        if "timeout" not in kwargs:
            kwargs["timeout"] = timeout
        return request_method(*args, **kwargs)

    return wrapped_request
