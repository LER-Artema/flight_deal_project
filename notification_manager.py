from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = "AC37076814600b7630646342bf21502bf3"
        self.auth_token = "8bb6dc5db6682418700cf56715c47c09"
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self):
        self.client.messages \
            .create(
                body="aaa",
                from_='+14154170291',
                to='+525522494955'
            )
