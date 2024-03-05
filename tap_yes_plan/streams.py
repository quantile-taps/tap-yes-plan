"""Stream type classes for tap-yes-plan."""

from singer_sdk import typing as th
from tap_yes_plan.client import YesPlanStream

user = [
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("username", th.StringType),
    th.Property("email", th.StringType),
    th.Property("hasBackOfficeAccess", th.BooleanType),
]

user_group = [
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
]

group = [
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
]

profile = [
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
]

status = [
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("statustypes", th.StringType),
]

location = [
    th.Property("id", th.StringType),
    th.Property("_type", th.StringType),
    th.Property("url", th.StringType),
    th.Property("name", th.StringType),
]

event = [
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("group", th.ObjectType(*group)),
    th.Property("defaultscheduledescription", th.StringType),
    th.Property("defaultschedulestarttime", th.StringType),
    th.Property("defaultscheduleendtime", th.StringType),
    th.Property("defaultschedulestart", th.StringType),
    th.Property("defaultscheduleend", th.StringType),
    th.Property("status", th.ObjectType(*status)),
    th.Property("profile", th.ObjectType(*profile)),
    th.Property("locations", th.ArrayType(th.ObjectType(*location))),
    th.Property("starttime", th.DateTimeType),
    th.Property("endtime", th.DateTimeType),
    th.Property("isproduction", th.BooleanType),
    th.Property("owner", th.ObjectType(*user)),
    th.Property("owningteam", th.ObjectType(*user_group)),
    th.Property("owninggroup", th.ObjectType(*user_group)),
    th.Property("parentgroup", th.ObjectType(*group)),
]

resource = [
    th.Property("_type", th.StringType),
    th.Property("id", th.StringType),
    th.Property("resourcetype", th.StringType),
    th.Property("name", th.StringType),
    th.Property("group", th.StringType),
    th.Property("url", th.StringType),
]

resource_booking = [
    th.Property("url", th.StringType),
    th.Property("id", th.StringType),
    th.Property("_type", th.StringType),
]

resource_booking_with_resource = [
    *resource_booking,
    th.Property("resource", th.ObjectType(*resource))
]

vat_per_rate = [
    th.Property("vatpercentage", th.NumberType),
    th.Property("vat", th.NumberType),
    th.Property("netprice", th.NumberType),
    th.Property("price", th.NumberType),
]

cost_model = [
    th.Property("name", th.StringType),
    th.Property("cost", th.StringType),
    th.Property("costformula", th.ObjectType(
        th.Property("amount", th.NumberType),
        th.Property("includesvat", th.BooleanType),
    )),
    th.Property("price", th.StringType),
    th.Property("priceformula", th.ObjectType(
        th.Property("amount", th.NumberType),
        th.Property("includesvat", th.BooleanType),
    )),
    th.Property("account", th.StringType),
    th.Property("invoice", th.BooleanType),
    th.Property("durationdiscount",
                th.ObjectType(
                    th.Property("type", th.StringType),
                    th.Property("notation", th.StringType),
                    th.Property(
                        "rates",
                        th.ArrayType(
                            th.ArrayType(
                                th.NumberType
                            )
                        )
                    )
                ),
                ),
    th.Property("volumediscount",
                th.ObjectType(
                    th.Property("type", th.StringType),
                    th.Property("notation", th.StringType),
                    th.Property(
                        "rates",
                        th.ArrayType(
                            th.ArrayType(
                                th.NumberType
                            )
                        )
                    )
                ),
                ),
    th.Property("purchaseprice", th.NumberType),
    th.Property("vat", th.NumberType),
    th.Property("profiles", th.ArrayType(th.ObjectType(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
    ))),
]

resource_costings = [
    th.Property(
        "resource",
        th.ObjectType(*resource)
    ),
    th.Property(
        "resourcebooking",
        th.ObjectType(*resource_booking),
    ),
    th.Property("alteration", th.ObjectType(
        th.Property("price", th.StringType),
        th.Property("netprice", th.StringType),
        th.Property("vatinclusive", th.BooleanType),
    )),
    th.Property("cost", th.NumberType),
    th.Property("netprice", th.NumberType),
    th.Property("margin", th.NumberType),
    th.Property("vat", th.NumberType),
    th.Property(
        "vatperrate",
        th.ArrayType(
            th.ObjectType(*vat_per_rate)
        )
    ),
    th.Property("price", th.NumberType),
    th.Property("netpricebeforediscount", th.NumberType),
    th.Property("pricebeforediscount", th.NumberType),
    th.Property("discountpercentage", th.StringType),
    th.Property("costmodel", th.ObjectType(*cost_model)),
    th.Property("invoice", th.BooleanType),
    th.Property("actualalteration", th.ObjectType(
        th.Property("price", th.StringType),
        th.Property("netprice", th.StringType),
        th.Property("vatinclusive", th.BooleanType),
    )),
    th.Property("actualcost", th.NumberType),
    th.Property("actualnetprice", th.NumberType),
    th.Property("actualmargin", th.NumberType),
    th.Property("actualvat", th.NumberType),
    th.Property(
        "actualvatperrate",
        th.ArrayType(
            th.ObjectType(*vat_per_rate)
        )
    ),
    th.Property("actualprice", th.NumberType),
    th.Property("actualnetpricebeforediscount", th.NumberType),
    th.Property("actualpricebeforediscount", th.NumberType),
    th.Property("actualdiscountpercentage", th.StringType),
]

costings = [
    th.Property("alteration", th.ObjectType(
        th.Property("price", th.StringType),
        th.Property("netprice", th.StringType),
        th.Property("vatinclusive", th.BooleanType),
    )),
    th.Property(
        "resourcecostings",
        th.ArrayType(
            th.ObjectType(*resource_costings)
        )
    ),
    th.Property("group", th.StringType),
    th.Property("cost", th.NumberType),
    th.Property("netprice", th.NumberType),
    th.Property("margin", th.NumberType),
    th.Property("vat", th.NumberType),
    th.Property(
        "vatperrate",
        th.ArrayType(
            th.ObjectType(*vat_per_rate)
        )
    ),
    th.Property("price", th.NumberType),
    th.Property("netpricebeforediscount", th.NumberType),
    th.Property("pricebeforediscount", th.NumberType),
    th.Property("discountpercentage", th.StringType),
    th.Property("actualalteration", th.ObjectType(
        th.Property("price", th.StringType),
        th.Property("netprice", th.StringType),
        th.Property("vatinclusive", th.BooleanType),
    )),
    th.Property("actualcost", th.NumberType),
    th.Property("actualnetprice", th.NumberType),
    th.Property("actualmargin", th.NumberType),
    th.Property("actualvat", th.NumberType),
    th.Property(
        "actualvatperrate",
        th.ArrayType(
            th.ObjectType(*vat_per_rate)
        )
    ),
    th.Property("actualprice", th.NumberType),
    th.Property("actualnetpricebeforediscount", th.NumberType),
    th.Property("actualpricebeforediscount", th.NumberType),
    th.Property("actualdiscountpercentage", th.StringType),
]

contact = [
        th.Property("id", th.StringType),
        th.Property("contact", th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("_type", th.StringType),
        ))
]

attachment = [
    th.Property("comment", th.StringType),
    th.Property("dataurl", th.StringType),
    th.Property("date", th.DateType),
    th.Property("username", th.StringType),
]

class EventsStream(YesPlanStream):
    """Stream that fetches all the different events."""

    name = "events"
    path = "/events/date:01-01-2024 TO 01-03-2024/"
    primary_keys = ["id"]
    replication_key = None

    default_schema = th.PropertiesList(
        th.Property("id", th.StringType),
    ).to_dict()


class EventsCustomStream(YesPlanStream):
    """This stream fetches all custom data related to events."""

    name = "events_custom_data"
    path = "/events/date:01-01-2024 TO 01-03-2024/customdata?valuesonly"
    primary_keys = ["event_id"]
    replication_key = None

    def post_process(self, row: dict, context: dict) -> dict:
        row["event_id"] = row["event"]["id"]
        return row

    default_schema = th.PropertiesList(
        th.Property("event_id", th.StringType),
    ).to_dict()


class EventsCostingsStream(YesPlanStream):
    """This stream fetches all custom data related to events."""

    name = "events_costings"
    path = "/events/date:01-01-2024 TO 31-12-2024/costings"
    primary_keys = ["event_id"]
    replication_key = None

    def post_process(self, row: dict, context: dict) -> dict:
        row["event_id"] = row["event"]["id"]
        return row

    default_schema = th.PropertiesList(
        th.Property("event_id", th.StringType),
        th.Property(
            "costings",
            th.ArrayType(
                th.ObjectType(
                    *costings
                ),
            ),
        ),
    ).to_dict()
