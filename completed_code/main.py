import requests

from config import WEATHER_API_KEY, LAT, LON, SLACK_WEBHOOK_URL, YOUR_FULL_NAME

def format_message(text):
    return {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": YOUR_FULL_NAME
                }
            },
            {
                "type": "section",
                
                "text": {
                    "type": "plain_text",
                    "text": text
                }
            }
        ]
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


def get_weather(lat=LAT, lon=LON, exclude=['minutely, hourly, daily']):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={(',').join(exclude)}&appid={WEATHER_API_KEY}&units=imperial")
    data = r.json()
    return f"The temperature is currently {str(data['current']['temp'])} and outside there are {data['current']['weather'][0]['description']}."


def main(event=None, context=None):
    weather = get_weather()
    message = format_message(weather)
    send_message(message)


if __name__ == "__main__":
    main()