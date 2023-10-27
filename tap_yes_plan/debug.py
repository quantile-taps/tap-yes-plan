from dotenv import dotenv_values
from tap_yes_plan.tap import TapYesPlan

if __name__ == "__main__":
    env = dotenv_values("/schouwburg/.env")
    tap = TapYesPlan(
        {
            "api_key": env["YES_PLAN_API_KEY"],
            "url_base": "https://theater.yesplan.nl/api",
            "start_date": "2022-01-01",
        }
    )
    tap.sync_all()
