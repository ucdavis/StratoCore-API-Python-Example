"""Configuration settings to be imported by pyppms."""

# the URL of the PUMAPI to talk to:
PUMAPI_URL = "https://SERVER_URL/pumapi/"

# API key with appropriate permissions to run the desired commands. Store this as an OS enviromental variable named "PUMAPI_KEY":
PUMAPI_KEY = os.environ["PUMAPI_KEY"]

# requests timeout in seconds (default=10)
TIMEOUT = 10

# path where to cache responses (either relative to the repository root or an
# absolute path), can be empty which will disable the cache
CACHE_PATH = "tests/cached_responses"

# TESTING ONLY: path to mocked responses (either relative to the repository root or an
# absolute path)
MOCKS_PATH = "tests/mocked_responses"
