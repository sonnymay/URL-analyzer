import re
from urllib.parse import urlparse

def is_valid_url(url):
    """
    Checks if the URL is valid.

    Args:
    - url: The URL to be validated.
    
    Returns:
    - True if URL is valid, False otherwise.
    """
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None


def analyze_url(url):
    """
    Analyzes a given URL and extracts its different parts.

    Args:
    - url: The URL to be analyzed.
    
    Returns:
    - A dictionary containing different parts of the URL.
    """
    # Validate the URL
    if not is_valid_url(url):
        return "Invalid URL"

    # Parse the URL
    parsed_url = urlparse(url)
    
    # Extract different parts
    url_analysis = {
        'scheme': parsed_url.scheme,
        'netloc': parsed_url.netloc,
        'path': parsed_url.path,
        'params': parsed_url.params,
        'query': parsed_url.query,
        'fragment': parsed_url.fragment,
        'username': parsed_url.username,
        'password': parsed_url.password,
        'hostname': parsed_url.hostname,
        'port': parsed_url.port,
    }
    return url_analysis

# Example usage
url = "https://example.com:8080/path/to/resource?param1=value1&param2=value2#anchor"
analysis = analyze_url(url)
print(analysis)
