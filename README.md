### A reminder app with Python, Twilio and AWS Lambda

The script uses Python, Twilio and AWS Lambda to send a reminder message via WhatsApp message to designated recipients for pre-configured reminders.

Pre-requisites to run this script
1. Register with Twilio and set up the Twilio Sandbox for WhatsApp. This step will include setting up those users who will be recipients of the message sent by the Python script
2. Make a note of the sandbox Account SID and the Auth Token for the registred Twilio account
3. Create a virtual environment and install the requirements
4. Replace the recipient names and phone numbers (with the country code) in the directory.json file
5. Add the event details like the event name, due date and frequency (monthly / yearly) in the reminder_events.json file 
6. Zip the .py and .json files with the entire contents of ../venv/Lib/site-packages
7. Register with AWS, create a new lambda function for the Python 3.7 runtime and upload the zip file created in the previous step
8. Set the account_sid and auth_token environment variables on the AWS console using the values from step 2. Set the handler as *reminders.check_appointments*
9. Once the function is saved, add a CloudWatch Event trigger on the console to run the script at the desired time. I have used a cron(30 1 * * ? *) command to run the script at 1:30 AM UTC (7 AM IST) :clock7:
10. A pre-defined Twilio sandbox message template (`Your appointment is coming up on {{1}} at {{2}}`) has been used to configure the body of the message. Using this template overcomes the 24 hours limition set by the sandbox

A sample message would look something like this - 

![IOS_Message](https://github.com/AbhishekPednekar84/reminder_app_twilio_aws_lambda/blob/master/images/Image%20from%20iOS.jpg)
