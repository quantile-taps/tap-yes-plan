"""REST client handling, including YesPlanStream base class."""
from typing import Iterable
from urllib.parse import parse_qs, urlparse

import requests
from singer_sdk.authenticators import APIKeyAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream


class YesPlanStream(RESTStream):
    """YesPlan stream class."""

    url_base = "https://theaterhaarlem.yesplan.nl/api"
    records_jsonpath = "$.data[*]"
    next_page_token_jsonpath = "$.pagination.next"

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object."""
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="api_key",
            value=self.config.get("api_key"),
            location="params",
        )

    def extract_params(self, url) -> dict:
        """Extract all params from an url."""
        parsed_url = urlparse(url)
        return parse_qs(parsed_url.query)

    def get_url_params(self, _context: dict, next_page_token: dict) -> dict[str]:
        """Return the next page token as url params."""
        return self.extract_params(next_page_token)

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records."""
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())
