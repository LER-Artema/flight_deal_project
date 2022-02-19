from twilio.rest import Client
import os

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.environ.get('account_id')
        self.auth_token = os.environ.get('account_token')
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self):
        self.client.messages \
            .create(
                body="aaa",
                from_='+14154170291',
                to='+525522494955'
            )
