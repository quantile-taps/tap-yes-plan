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
                th.Property("production_performer", th.StringType),
                th.Property("production_title", th.StringType),
                th.Property("production_subtitle", th.StringType),
                th.Property("samenvatting_ondertitel", th.StringType),
                th.Property("production_genre_intern", th.StringType),
                th.Property("production_subgenre", th.StringType),
                th.Property("production_typeshow", th.StringType),
                th.Property("production_duration", th.StringType),
                th.Property("production_pauze", th.StringType),
                th.Property("production_pauze_timebefore", th.StringType),
                th.Property("production_pauze_timeafter", th.StringType),
                th.Property("production_language", th.StringType),
                th.Property("production_inter_national", th.StringType),
                th.Property("production_gesubsidieerd", th.StringType),
                th.Property("production_surtitles", th.StringType),
                th.Property("production_framework", th.StringType),
                th.Property("production_general_remarks", th.StringType),
                th.Property("contract_contractadres", th.StringType),
                th.Property("contract_maker", th.StringType),
                th.Property("contract_maker_contact", th.ObjectType(*contact)),
                th.Property("contract_sent", th.StringType),
                th.Property("contract_signed", th.StringType),
                th.Property("contract_received", th.StringType),
                th.Property("contract_attachement", th.StringType),
                th.Property("contract_remarks", th.StringType),
                th.Property("contact_programmer", th.ObjectType(*contact)),
                th.Property("contact_productionmanager", th.ObjectType(*contact)),
                th.Property("contact_technics", th.ObjectType(*contact)),
                th.Property("contact_remarks_intern", th.ObjectType(*contact)),
                th.Property("contact_impressario", th.ObjectType(*contact)),
                th.Property("contact_impressario_contact", th.ObjectType(*contact)),
                th.Property("contact_client", th.ObjectType(*contact)),
                th.Property("contact_client_contact", th.ObjectType(*contact)),
                th.Property("production_samenwerking_met", th.ObjectType(*contact)),
                th.Property("contact_recordcomp_label", th.ObjectType(*contact)),
                th.Property("contact_performer", th.ObjectType(*contact)),
                th.Property("contact_producer", th.ObjectType(*contact)),
                th.Property("contact_invoice", th.ObjectType(*contact)),
                th.Property("contact_co_producer", th.ObjectType(*contact)),
                th.Property("contact_production", th.ObjectType(*contact)),
                th.Property("contact_communications", th.ObjectType(*contact)),
                th.Property("contact_technics_external", th.ObjectType(*contact)),
                th.Property("contact_roadie", th.ObjectType(*contact)),
                th.Property("contact_remarks_external", th.ObjectType(*contact)),
                th.Property("contract_bordereladres", th.StringType),
                th.Property("contract_factuuradres", th.StringType),
                th.Property("contract_borderelverstuurd", th.StringType),
                th.Property("contract_datumborderel", th.StringType),
                th.Property("contract_factuurgetekend", th.StringType),
                th.Property("contract_auteursrechtbetaald", th.StringType),
                th.Property("contract_extrabijlageveld", th.StringType),
                th.Property("contract_notes_borderelfactuur", th.StringType),
                th.Property("contract_prafspraken", th.StringType),
                th.Property("contract_techniek", th.StringType),
                th.Property("contract_dressingroom", th.StringType),
                th.Property("contract_hotel_info", th.StringType),
                th.Property("contract_hotel", th.StringType),
                th.Property("contract_catering", th.StringType),
                th.Property("contract_catering_info", th.StringType),
                th.Property("contract_transport", th.StringType),
                th.Property("contract_transport_info", th.StringType),
                th.Property("contract_content_remarks", th.StringType),
                th.Property("promo_program_short", th.StringType),
                th.Property("production_genre", th.StringType),
                th.Property("promo_geannuleerd", th.StringType),
                th.Property("promo_exporteernaarcmswebsite_oud", th.StringType),
                th.Property("promo_titel", th.StringType),
                th.Property("promo_ondertitel", th.StringType),
                th.Property("promo_typevoorstelling", th.StringType),
                th.Property("promo_genres", th.ArrayType(th.StringType)),
                th.Property("promo_subgenres", th.StringType),
                th.Property("promo_labels", th.StringType),
                th.Property("promo_servicekosten", th.StringType),
                th.Property("promo_program", th.StringType),
                th.Property("promo_credits", th.StringType),
                th.Property("promo_budget", th.StringType),
                th.Property("promo_budget_remarks", th.StringType),
                th.Property("promo_planimpresariaat", th.StringType),
                th.Property("promo_plan", th.StringType),
                th.Property("promo_pers_dagbladen", th.StringType),
                th.Property("promo_twosignsframesa2ronde", th.StringType),
                th.Property("promo_adwordsgooglegrants", th.StringType),
                th.Property("promo_facebookcampagne", th.StringType),
                th.Property("publiciteitsmateriaal_aangevraagda0", th.StringType),
                th.Property("publiciteitsmateriaal_binnengekomena0", th.StringType),
                th.Property("publiciteitsmateriaal_aangevraagda2", th.StringType),
                th.Property("publiciteitsmateriaal_binnengekomena2", th.StringType),
                th.Property("publiciteitsmateriaal_aangevraagdflyersa5", th.StringType),
                th.Property("publiciteitsmateriaal_binnengekomenflyersa5", th.StringType),
                th.Property("publiciteitsmateriaal_financieleafsprakenprmateriaal", th.StringType),
                th.Property("production_rider_hospitality", th.StringType),
                th.Property("production_rider_technical", th.StringType),
                th.Property("production_press", th.StringType),
                th.Property("production_prie", th.StringType),
                th.Property("production_lightplan", th.StringType),
                th.Property("production_kaplijst", th.StringType),
                th.Property("production_extra", th.StringType),
                th.Property("production_remarks", th.StringType),
                th.Property("promo_artwork_text", th.StringType),
                th.Property("promo_artwork_required", th.StringType),
                th.Property("promo_artwork_received", th.StringType),
                th.Property("promo_artwork_pressphoto", th.StringType),
                th.Property("promo_remarks", th.StringType),
                th.Property("licenses_nightpermit", th.StringType),
                th.Property("licenses_remarks", th.StringType),
                th.Property("rental_date_request", th.StringType),
                th.Property("rental_enddate_request", th.StringType),
                th.Property("rental_name", th.StringType),
                th.Property("rental_type", th.StringType),
                th.Property("rental_type_other", th.StringType),
                th.Property("rental_public_remarks", th.StringType),
                th.Property("rental_referral", th.StringType),
                th.Property("rental_reference_other", th.StringType),
                th.Property("rental_eigentekstbrief", th.StringType),
                th.Property("rental_letter_catering", th.StringType),
                th.Property("rental_letter_catering_intern", th.StringType),
                th.Property("rental_letter_techniek", th.StringType),
                th.Property("rental_letter_techniek_intern", th.StringType),
                th.Property("rental_letter_opbouw", th.StringType),
                th.Property("rental_letter_opbouw_intern", th.StringType),
                th.Property("rental_letter_algemeen", th.StringType),
                th.Property("rental_letter_algemene_intern", th.StringType),
                th.Property("rental_offer_signed", th.StringType),
                th.Property("rental_offer_signed_attachement", th.StringType),
                th.Property("rental_advance", th.StringType),
                th.Property("rental_advance_date", th.StringType),
                th.Property("rental_advance_amount", th.StringType),
                th.Property("rental_advance_invoice", th.StringType),
                th.Property("rental_annulation_fee", th.StringType),
                th.Property("doorteberekenen_doorberekenenimpresariaat", th.StringType),
                th.Property("doorteberekenen_bijlage1", th.StringType),
                th.Property("doorteberekenen_bijlage2", th.StringType),
                th.Property("doorteberekenen_bijlage3", th.StringType),
                th.Property("borderel_aantalbezoekers", th.StringType),
                th.Property("borderel_brutokaartverkoop", th.StringType),
                th.Property("borderel_horecatoeslag", th.IntegerType),
                th.Property("borderel_horecatoeslagpodiumpas", th.StringType),
                th.Property("borderel_theatertoeslag", th.IntegerType),
                th.Property("borderel_theatertoeslagpodiumpas", th.StringType),
                th.Property("borderel_brutorecette", th.IntegerType),
                th.Property("borderel_btw6", th.IntegerType),
                th.Property("borderel_nettorecette", th.IntegerType),
                th.Property("borderel_auteursrechtrecette", th.IntegerType),
                th.Property("borderel_auteursrecht", th.IntegerType),
                th.Property("borderel_partagebasis", th.IntegerType),
                th.Property("borderel_1eaandeelbespeler", th.IntegerType),
                th.Property("borderel_garantie", th.StringType),
                th.Property("borderel_aanvullingtotuitkoop", th.IntegerType),
                th.Property("borderel_aanvullingtotgarantie", th.IntegerType),
                th.Property("borderel_2eaandeelbespeler", th.IntegerType),
                th.Property("borderel_aandeelbespeler", th.NumberType),
                th.Property("borderel_btw6factuurditbedrag", th.IntegerType),
                th.Property("borderel_btw6factuur", th.NumberType),
                th.Property("borderel_btw21factuur", th.NumberType),
                th.Property("borderel_factuurbedrag", th.NumberType),
                th.Property("deal_dealdefinitief", th.ArrayType(th.StringType)),
                th.Property("financial_participation_txt", th.StringType),
                th.Property("deal_typedeal", th.StringType),
                th.Property("deal_partage", th.IntegerType),
                th.Property("deal_partage2", th.IntegerType),
                th.Property("deal_trapgrens", th.IntegerType),
                th.Property("deal_garantiesom", th.IntegerType),
                th.Property("deal_uitkoop", th.IntegerType),
                th.Property("deal_huurbedrag", th.IntegerType),
                th.Property("deal_auteursrechten", th.IntegerType),
                th.Property("deal_auteursrechten_uitzonderlijk", th.StringType),
                th.Property("financial_remittance", th.StringType),
                th.Property("deal_pki", th.StringType),
                th.Property("deal_overigekostenimpresariaat", th.StringType),
                th.Property("deal_notitiesoverigekostenimpresariaat", th.StringType),
                th.Property("deal_maxverliesbijdrage", th.IntegerType),
                th.Property("deal_suppletietotbovengrens", th.StringType),
                th.Property("financial_discount", th.StringType),
                th.Property("sales_verwachtbezetingspercentage", th.NumberType),
                th.Property("financial_buma_stemra_sabam", th.StringType),
                th.Property("deal_datelastupdate", th.DateType),
                th.Property("deal_remarks", th.StringType),
                th.Property("visitors_expectation", th.StringType),
                th.Property("visitors_notes", th.StringType),
                th.Property("sales_capacity_rang1", th.IntegerType),
                th.Property("sales_capacity_rang2", th.IntegerType),
                th.Property("sales_capacity_rang3", th.IntegerType),
                th.Property("sales_capacity_toprang", th.IntegerType),
                th.Property("sales_expectation", th.IntegerType),
                th.Property("sales_werkelijkaantalbezoekers", th.StringType),
                th.Property("sales_expectation_adjusted", th.StringType),
                th.Property("sales_expectation_adjusted2", th.StringType),
                th.Property("sales_remarks", th.StringType),
                th.Property("bezoekers_aantaldeelnemersstadsprogammering", th.StringType),
                th.Property("eventiditheatre", th.StringType),
                th.Property("importimpresariaat", th.StringType),
                th.Property("contractontvangen", th.StringType),
                th.Property("rolstoelplaatsen", th.StringType),
                th.Property("yesplanidvoorupsell_inleiding", th.StringType),
                th.Property("yesplanidvoorupsell_etenendrinken", th.StringType),
                th.Property("yesplanidvoorupsell_extra", th.StringType),
                th.Property("yesplanidvoorupsell_pauzearrangementen", th.StringType),
                th.Property("yesplanidvoorupsell_naborrelarrangement", th.StringType),
                th.Property("yesplanidvoorupsell_arrangementextra", th.StringType),
                th.Property("yesplanidvoorupsell_pauze", th.StringType),
                th.Property("evenement_yesplanidvoorupsell_einde", th.StringType),
                th.Property("event_voorstellingsinformatie_infovooraf", th.StringType),
                th.Property("evenement_rolstoel", th.StringType),
                th.Property("event_voorstellingsinformatie_verslag", th.StringType),
                th.Property("event_voorstellingsinformatie_theaterdienst", th.StringType),
                th.Property("event_voorstellingsinformatie_toneelmeester", th.StringType),
                th.Property("evenement_voorstellingsinformatie_portier", th.StringType),
                th.Property("horecainformatie_checklisthoreca", th.StringType),
                th.Property("horecainformatie_horecaevaluatie", th.StringType),
                th.Property("horecainformatie_gebruiktedrankjes", th.StringType),
                th.Property("artists_number", th.StringType),
                th.Property("artists_bloemen", th.StringType),
                th.Property("artists_remarks", th.StringType),
                th.Property("crew_aankomsttijdtechniek", th.StringType),
                th.Property("crew_number", th.StringType),
                th.Property("crew_aantaltechnicizt", th.StringType),
                th.Property("crew_type", th.StringType),
                th.Property("crew_building_number", th.StringType),
                th.Property("crew_shutdown_number", th.StringType),
                th.Property("venue_seating", th.StringType),
                th.Property("venue_orchestrapit", th.StringType),
                th.Property("venue_zaalopstelling_balkonopen", th.StringType),
                th.Property("venue_stage", th.StringType),
                th.Property("sales_capacity", th.StringType),
                th.Property("evenement_rija", th.StringType),
                th.Property("venue_opmerkingzaalopstelling", th.StringType),
                th.Property("venue_setup_plan", th.StringType),
                th.Property("venue_remarks", th.StringType),
                th.Property("calendar_movedto", th.StringType),
                th.Property("calendar_cancelled_info", th.StringType),
                th.Property("calendar_remarks", th.StringType),
                th.Property("guestlist_intern", th.StringType),
                th.Property("guestlist_intern_names", th.StringType),
                th.Property("guestlist_impresario", th.StringType),
                th.Property("guestlist_impresario_names", th.StringType),
                th.Property("guestlist_number", th.StringType),
                th.Property("guestlist_names", th.StringType),
                th.Property("technical_light", th.StringType),
                th.Property("technical_light_show", th.StringType),
                th.Property("technical_light_remarks", th.StringType),
                th.Property("technical_sound", th.StringType),
                th.Property("technical_sound_mengtafel", th.StringType),
                th.Property("technical_sound_remarks", th.StringType),
                th.Property("technical_recording", th.StringType),
                th.Property("technical_recording_remarks", th.StringType),
                th.Property("technical_projection", th.StringType),
                th.Property("technical_projection_source", th.StringType),
                th.Property("technical_projection_remarks", th.StringType),
                th.Property("pyro_smoke", th.StringType),
                th.Property("pyro_pyro", th.StringType),
                th.Property("pyro_fire", th.StringType),
                th.Property("pyro_firedep_informed", th.StringType),
                th.Property("pyro_remarks", th.StringType),
                th.Property("toneel_kameelmeester", th.StringType),
                th.Property("toneel_balletvloer", th.StringType),
                th.Property("toneel_afstopping", th.StringType),
                th.Property("toneel_vleugel", th.StringType),
                th.Property("toneel_tijdstipstemmen", th.StringType),
                th.Property("toneel_opmerkingen", th.StringType),
                th.Property("transport_forth", th.StringType),
                th.Property("transport_back", th.StringType),
                th.Property("transport_remarks", th.StringType),
                th.Property("parking_provide", th.StringType),
                th.Property("parking_cars", th.StringType),
                th.Property("parking_busses", th.StringType),
                th.Property("parking_trucks", th.StringType),
                th.Property("parking_remarks", th.StringType),
                th.Property("cleaning_remarks", th.StringType),
                th.Property("log_technic", th.StringType),
                th.Property("log_horeca", th.StringType),
                th.Property("log_paydesk", th.StringType),
                th.Property("log_crowd_assistance", th.StringType),
                th.Property("log_maintenance", th.StringType),
                th.Property("vrijwilligers_aantal", th.StringType),
                th.Property("vrijwilligers_ingeroosterdevrijwilligers", th.StringType),
                th.Property("vrijwilligers_backstagegastvrouw", th.StringType),
                th.Property("vrijwilligers_buitenportier", th.StringType),
                th.Property("merchandise_seller", th.StringType),
                th.Property("merchandise_payment", th.StringType),
                th.Property("merchandise_agreement", th.StringType),
                th.Property("merchandise_seller_external", th.StringType),
                th.Property("merchandise_seller_external_contact", th.StringType),
                th.Property("merchandise_remarks", th.StringType),
                th.Property("ticketmatic_trigger", th.StringType),
                th.Property("ticketmatic3_totaltickets", th.StringType),
                th.Property("ticketmatic3_freetickets", th.StringType),
                th.Property("ticketmatic3_lockedsoft", th.StringType),
                th.Property("ticketmatic3_lockedhard", th.StringType),
                th.Property("ticketmatic3_soldpaid", th.StringType),
                th.Property("ticketmatic3_soldunpaid", th.StringType),
                th.Property("ticketmatic3_reserved", th.StringType),
                th.Property("ticketmatic3_complimentary", th.StringType),
                th.Property("ticketmatic3_ticketsalesamount", th.StringType),
                th.Property("ticketmatic3_ticketfeeamount", th.StringType),
                th.Property("ticketmatic3_totalsalesamount", th.StringType),
                th.Property("ticketmatic3_ticketsnotscanned", th.StringType),
                th.Property("ticketmatic3_ticketsscanned", th.StringType),
                th.Property("ticketmatic3_ticketsscannedexit", th.StringType),
                th.Property("first_aid", th.StringType),
                th.Property("first_aid_contact", th.StringType),
                th.Property("first_aid_remarks", th.StringType),
                th.Property("security", th.StringType),
                th.Property("security_number", th.StringType),
                th.Property("security_contact", th.StringType),
                th.Property("security_remarks", th.StringType),
                th.Property("ongevallenrapport_plaatsruimte", th.StringType),
                th.Property("ongevallenrapport_datum", th.StringType),
                th.Property("ongevallenrapport_tijdstip", th.StringType),
                th.Property("ongevallenrapport_naamevent", th.StringType),
                th.Property("ongevallenrapport_rapportgemaaktdoor", th.StringType),
                th.Property("ongevallenrapport_naambetrokkene", th.StringType),
                th.Property("ongevallenrapport_adresbetrokkene", th.StringType),
                th.Property("ongevallenrapport_telefoonbetrokkene", th.StringType),
                th.Property("ongevallenrapport_omschrijfdegebeurtenis", th.StringType),
                th.Property("ongevallenrapport_betrokkenpersoneel", th.StringType),
                th.Property("ongevallenrapport_anderebetrokkenen", th.StringType),
                th.Property("ongevallenrapport_welkehulpdiensten", th.StringType),
                th.Property("ongevallenrapport_anderehulpdienstnl", th.StringType),
                th.Property("ongevallenrapport_rolbhv", th.StringType),
                th.Property("ongevallenrapport_opmerkingen", th.StringType),
                th.Property("boekhouding_kostenplaats", th.StringType),
                th.Property("boekhouding_aanvullendeinformatieboekhouding", th.StringType),
                th.Property("boekhouding_vismaeventid", th.StringType),
                th.Property("promo_exporteernaarcmswebsite", th.ArrayType(th.StringType)),
                th.Property("sales_ticketprice_standard", th.NumberType),
                th.Property("ticketprice_afrekenen_2", th.NumberType),
                th.Property("ticketprice_afrekenen_3", th.NumberType),
                th.Property("ticketprice_afrekenen_toprang", th.NumberType),
                th.Property("sales_ticketprice_theatreallowance", th.NumberType),
                th.Property("sales_ticketprice_drinksallowance", th.NumberType),
                th.Property("sales_ticketprice_cloakroomallowance", th.StringType),
                th.Property("sales_ticketprice_reservationcosts", th.StringType),
                th.Property("sales_ticketprice_price1", th.NumberType),
                th.Property("sales_ticketprice_price2", th.NumberType),
                th.Property("sales_ticketprice_price3", th.NumberType),
                th.Property("sales_ticketprice_price4", th.NumberType),
                th.Property("ticketprice_toegang_1", th.NumberType),
                th.Property("ticketprice_toegang_2", th.NumberType),
                th.Property("ticketprice_toegang_3", th.NumberType),
                th.Property("ticketprice_toegang_toprang", th.NumberType),
                th.Property("sales_ticketprijzen_verkoopdoor", th.StringType),
                th.Property("sales_ticketprijzen_verkoopopinternet", th.StringType),
                th.Property("sales_ticketprijzen_inclusiefservicekosten", th.StringType),
                th.Property("sales_ticketprijzen_inclusiefservicekosten_oud", th.StringType),
                th.Property("sales_ticketprijzen_rolstoelplaatsenverkochtdoor", th.StringType),
                th.Property("sales_ticketprijzen_opmerkingennotities", th.StringType),
                th.Property("appconnex_debtor", th.StringType),
                th.Property("afasproject_referentie", th.StringType),
                th.Property("production_title1", th.StringType),
                th.Property("contacts_internal_booker", th.StringType),
                th.Property("contacts_external_organizer_organization", th.StringType),
                th.Property("contacts_external_organizer_person", th.StringType),
                th.Property("quote_letter_personalized_note", th.StringType),
                th.Property("quote_additional_info", th.StringType),
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
