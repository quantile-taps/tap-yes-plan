"""YesPlan tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th
from tap_yes_plan import streams

STREAM_TYPES = [
    # streams.EventsStream,
    # streams.EventsCustomStream,
    streams.EventsCostingsStream,
]


class TapYesPlan(Tap):
    """Yes Plan tap class."""

    name = "tap-yes-plan"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "url_base",
            th.StringType,
            required=True,
            description="The url base of the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapYesPlan.cli()
