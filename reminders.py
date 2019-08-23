import json
import os
from twilio.rest import Client
from datetime import datetime


def check_appointments(event=None, context=None):
    """This method reads the reminder_events.json file to determine if any of the monthly or annual reminders are due today. If yes, a call is made to the send_whatsapp_message() method to send an event reminder to the recipients listed in directory.json
    """

    # Extract the day and month from today's date
    current_day = datetime.today().day
    current_month = datetime.today().month

    # Sent the date format as Month, Day Ex: August, 21
    formatted_date = datetime.today().strftime("%B, %d")

    with open("reminder_events.json", "r") as f:
        reminders = json.load(f)

    # Read the event reminders from the reminders.json file
    for reminder in reminders["events"]:
        if reminder["frequency"] == "M":
            if reminder["due"] == str(current_day):
                send_whatsapp_message(reminder["title"], formatted_date)
        elif reminder["frequency"] == "Y":
            r_month, r_day = reminder["due"].split("-")

            if r_month == str(current_month) and r_day == str(current_day):
                send_whatsapp_message(reminder["title"], formatted_date)


def send_whatsapp_message(event_name, event_date):
    """The function will send a whatsapp message to the recipients listed in directory.json. A call will be made to the Twilio Whatsapp sandbox API to send the message. To overcome the 24 hour messaging window limitation of the sandbox, the following message template will be used -

    Your appointment is coming up on {{1}} at {{2}}

    Args:
        event_name (string): [the name of the event for which we are generating the reminder]
        event_date ([type]): [current date formated as Month, Day - Ex: August, 21]
    """

    # The SID and TOKEN values will be read from the AWS Lambda Console
    account_sid = os.environ["account_sid"]
    auth_token = os.environ["auth_token"]

    # Create the Twilio client object
    client = Client(account_sid, auth_token)

    event_name = f"10 AM ({event_name})"

    # Read the recipient data from the directory.json file
    with open("directory.json", "r") as f:
        recipients = json.load(f)

    for recipient in recipients["members"]:
        message = client.messages.create(
            body=f"Your appointment is coming up on {event_date} at {event_name}",
            from_="whatsapp:+14155238886",
            to=f"whatsapp:{recipient['phone']}",
        )
