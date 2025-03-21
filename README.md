# GroupMe Daily Frisbee Poll

This script automatically creates a "Daily Frisbee Checkin" poll in a specified GroupMe group every weekday (Monday-Friday) at 8:00 AM Pacific Time. The poll will not be created after 3:00 PM.

## Setup

1. Install the required dependencies:
pip install -r requirements.txt

2. Get your GroupMe API token:
   - Go to https://dev.groupme.com/
   - Log in with your GroupMe account
   - Go to "Access Token" and copy your token

3. Get your GroupMe group ID:
   - Go to https://dev.groupme.com/groups
   - Find your group and note its ID

4. Update the `daily_frisbee_poll.py` script with your API token and group ID.

## Running the Script

To run the script manually:
python3 daily_frisbee_poll.py


## Running as a Service

### On macOS:
Create a launchd plist file to run the script automatically at startup.

### On Linux:
Set up a systemd service or use cron to run the script automatically.

## Notes

- The poll is set to expire after 12 hours by default
- The script will not create polls on weekends
- The script will not create polls after 3:00 PM Pacific Time