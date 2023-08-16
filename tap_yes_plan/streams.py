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
    th.Property("type", th.StringType),
    th.Property("group", th.StringType),
    th.Property("description", th.StringType),
    th.Property("external", th.BooleanType),
    th.Property("rented", th.BooleanType),
    th.Property("amount", th.StringType),
]

event = [
    th.Property("id", th.StringType),
    th.Property("owner", th.ObjectType(*user)),
    th.Property("owningteam", th.ObjectType(*user_group)),
    th.Property("owninggroup", th.ObjectType(*user_group)),
    th.Property("name", th.StringType),
    th.Property("group", th.ObjectType(*group)),
    th.Property("parentgroup", th.ObjectType(*group)),
    th.Property("starttime", th.DateTimeType),
    th.Property("endtime", th.DateTimeType),
    th.Property("profile", th.ObjectType(*profile)),
    th.Property("status", th.ObjectType(*status)),
    th.Property("locations", th.ArrayType(th.ObjectType(*location))),
    th.Property("isproduction", th.BooleanType),
]

resource = [
    th.Property("url", th.StringType),
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("_type", th.StringType),
]

resource_booking = [
    th.Property("url", th.StringType),
    th.Property("id", th.StringType),
    th.Property("_type", th.StringType),
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
    th.Property("price", th.NumberType),
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
    th.Property("profiles", th.ArrayType(th.StringType)),
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
    th.Property("alteration", th.StringType),
    th.Property("cost", th.NumberType),
    th.Property("netprice", th.NumberType),
    th.Property("margin", th.StringType),
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
    th.Property("actualalteration", th.StringType),
    th.Property("actualcost", th.NumberType),
    th.Property("actualnetprice", th.NumberType),
    th.Property("actualmargin", th.StringType),
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
    th.Property("alteration", th.StringType),
    th.Property(
        "resourcecostings",
        th.ArrayType(
            th.ObjectType(*resource_costings)
        )
    ),
    th.Property("group", th.StringType),
    th.Property("cost", th.NumberType),
    th.Property("netprice", th.NumberType),
    th.Property("margin", th.StringType),
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
    th.Property("actualalteration", th.StringType),
    th.Property("actualcost", th.NumberType),
    th.Property("actualnetprice", th.NumberType),
    th.Property("actualmargin", th.StringType),
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


class EventsStream(YesPlanStream):
    """Stream that fetches all the different events."""

    name = "events"
    path = "/events"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(*event).to_dict()


class EventsCustomStream(YesPlanStream):
    """This stream fetches all custom data related to events."""

    name = "events_custom_data"
    path = "/events/date:01-01-1970 TO 31-12-2999/customdata?valuesonly"
    primary_keys = ["event__id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property(
            "event",
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("name", th.StringType),
            ),
        ),
        th.Property(
            "items",
            th.ObjectType(
                th.Property("kostendrager", th.StringType),
                th.Property("production_genre", th.StringType),
                th.Property("production_title", th.StringType),
                th.Property("production_performer", th.StringType),
                th.Property("sales_expectation_adjusted", th.IntegerType),
                th.Property("sales_definitief", th.IntegerType),
                th.Property("ticketmatic3_totaltickets", th.IntegerType),
                th.Property("ticketmatic3_freetickets", th.IntegerType),
                th.Property("ticketmatic3_capacity", th.IntegerType),
                th.Property("ticketmatic3_lockedsoft", th.IntegerType),
                th.Property("ticketmatic3_lockedhard", th.IntegerType),
                th.Property("ticketmatic3_soldpaid", th.IntegerType),
                th.Property("ticketmatic3_inbasket", th.IntegerType),
                th.Property("ticketmatic3_complimentary", th.IntegerType),
                th.Property("ticketmatic3_reserved", th.IntegerType),
                th.Property("ticketmatic3_reservedamount", th.IntegerType),
                th.Property("ticketmatic3_reservedfeeamount", th.IntegerType),
                th.Property("ticketmatic3_totalreservedamount",
                            th.IntegerType),
                th.Property("ticketmatic3_ticketsalesamount", th.IntegerType),
                th.Property("ticketmatic3_ticketfeeamount", th.IntegerType),
                th.Property("ticketmatic3_ticketsnotscanned", th.IntegerType),
                th.Property("ticketmatic3_ticketsscanned", th.IntegerType),
                th.Property("ticketmatic3_ticketsscannedexit", th.IntegerType),
                th.Property("sales_capacity_rang1", th.IntegerType),
                th.Property("sales_capacity_rang2", th.IntegerType),
                th.Property("sales_capacity_rang3", th.IntegerType),
                th.Property("sales_capacity_rang4", th.IntegerType),
                th.Property("sales_capacity_rang5", th.IntegerType),
                th.Property("sales_ticketprice_price1", th.NumberType),
                th.Property("sales_ticketprice_price2", th.NumberType),
                th.Property("sales_ticketprice_price3", th.NumberType),
                th.Property("sales_ticketprice_price4", th.NumberType),
                th.Property("sales_ticketprice_price5", th.NumberType),
                th.Property("sales_ticketprice_drinksallowance",
                            th.NumberType),
                th.Property("sales_ticketprice_cloakroomallowance",
                            th.NumberType),
                th.Property("deal_typedeal", th.StringType),
                th.Property("deal_partage", th.StringType),
                th.Property("deal_partage2", th.StringType),
                th.Property("deal_trapgrens", th.StringType),
                th.Property("deal_garantiesom", th.StringType),
                th.Property("deal_garantiehaarlem", th.StringType),
                th.Property("deal_uitkoop", th.IntegerType),
                th.Property("deal_huurbedrag", th.IntegerType),
                th.Property("deal_auteursrechten", th.StringType),
                th.Property("deal_auteursrechtenx100", th.StringType),
                th.Property("deal_remittance", th.StringType),
                th.Property("deal_maxverliesbijdrage", th.StringType),
                th.Property("deal_suppletietotbovengrens", th.StringType),
                th.Property("deal_datelastupdate", th.StringType),
            ),
        ),
    ).to_dict()


class EventsCostingsStream(YesPlanStream):
    """This stream fetches all custom data related to events."""

    name = "events_costings"
    path = "/events/date:01-01-1970 TO 31-12-2999/costings"
    primary_keys = ["event__id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property(
            "event",
            th.ObjectType(
                th.Property("url", th.StringType),
                th.Property("id", th.StringType),
                th.Property("name", th.StringType),
            ),
        ),
        th.Property(
            "costings",
            th.ArrayType(
                th.ObjectType(
                    *costings
                ),
            ),
        ),
    ).to_dict()
