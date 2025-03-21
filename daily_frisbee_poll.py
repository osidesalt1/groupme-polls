import os
import requests
import pytz
from datetime import datetime, timedelta

API_TOKEN = os.environ.get("GROUPME_API_TOKEN")
GROUP_ID = os.environ.get("GROUPME_GROUP_ID")

def get_next_weekday_3pm():
    la_tz = pytz.timezone('America/Los_Angeles')
    now = datetime.now(la_tz)
    
    # Calculate next weekday (Mon-Fri)
    next_day = now + timedelta(days=1)
    while next_day.weekday() >= 5:  # Skip weekends
        next_day += timedelta(days=1)
    
    # Set to 3 PM PT
    target_time = next_day.replace(hour=15, minute=0, second=0, microsecond=0)
    return target_time.astimezone(pytz.utc).timestamp()

def create_poll():
    expiration = int(get_next_weekday_3pm())
    
    poll_data = {
        "subject": "Daily Frisbee Checkin 🥏",
        "options": [{"title": "Yes"}, {"title": "No"}],
        "expiration": expiration,
        "type": "single",
        "visibility": "public"
    }

    headers = {"X-Access-Token": API_TOKEN}
    response = requests.post(
        f"https://api.groupme.com/v3/poll/{GROUP_ID}",
        json=poll_data,
        headers=headers
    )
    print(f"Status: {response.status_code}")

if __name__ == "__main__":
    create_poll()