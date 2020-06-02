import requests

from config import WEATHER_API_KEY, LAT, LON, SLACK_WEBHOOK_URL, YOUR_FULL_NAME

def format_message(text):
    return {
	    "blocks": []
    }


def send_message(message_json, debug=False):
    if debug:
        print(message_json)
    else:
        r = requests.post(SLACK_WEBHOOK_URL, json=message_json)

        if r.status_code != 200:
            raise Exception(
                f"something went wrong, got code {r.status_code} with {r.content}"
            )

def get_weather():
    return f"It is cold."


def main(event=None, context=None):
    weather = get_weather()
    message = format_message(weather)
    send_message(message)


if __name__ == "__main__":
    main()