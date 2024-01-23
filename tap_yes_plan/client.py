"""REST client handling, including YesPlanStream base class."""
from typing import Iterable
from urllib.parse import parse_qs, urlencode, urlsplit, urlunsplit, urlparse

import requests
from singer_sdk.authenticators import APIKeyAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream

def _add_parameters(initial_url: str, extra_parameters: dict) -> str:
    """Add parameters to an URL and return the new URL.

    Args:
        initial_url: The URL to add parameters to.
        extra_parameters: The parameters to add.

    Returns:
        The new URL with the parameters added.
    """
    scheme, netloc, path, query_string, fragment = urlsplit(initial_url)
    query_params = parse_qs(query_string, keep_blank_values=True)
    query_params.update(extra_parameters)

    new_query_string = urlencode(query_params, doseq=True)

    if 'valuesonly' in query_params and not query_params['valuesonly'][0]:
        new_query_string = new_query_string.replace('valuesonly=', 'valuesonly')

    return urlunsplit((scheme, netloc, path, new_query_string, fragment))

# Create a custom Authenticator class that inherits from APIKeyAuthenticator
class YesPlanAuthenticator(APIKeyAuthenticator):

    # Update the authenticate_request method to add the api_key to the request params
    def authenticate_request(
        self,
        request: requests.PreparedRequest,
    ) -> requests.PreparedRequest:
        """Authenticate a request.

        Args:
            request: A `request object`_.

        Returns:
            The authenticated request object.

        .. _request object:
            https://requests.readthedocs.io/en/latest/api/#requests.PreparedRequest
        """
        request.headers.update(self.auth_headers)

        if request.url:
            request.url = _add_parameters(request.url, self.auth_params)

        return request


class YesPlanStream(RESTStream):
    """YesPlan stream class."""

    records_jsonpath = "$.data[*]"
    next_page_token_jsonpath = "$.pagination.next"

    @property
    def url_base(self) -> str:
        """Return the url_base for the requests."""
        return self.config.get("url_base")

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object."""
        return YesPlanAuthenticator.create_for_stream(
            self,
            key="api_key",
            value=self.config.get("api_key"),
            location="params",
        )

    def extract_params(self, url) -> dict:
        """Extract all params from an url."""
        parsed_url = urlparse(url)
        return parse_qs(parsed_url.query)

    def get_url_params(self, _context: dict, next_page_token: dict) -> dict:
        """Return the next page token as url params."""
        return self.extract_params(next_page_token)

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records."""
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())
