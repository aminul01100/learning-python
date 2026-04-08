"""
there will be three options to send out notifications to  the user-
1. Email
2. SMS
3. Push Notification
"""
from abc import ABC, abstractmethod
from email_validator import validate_email, EmailNotValidError


class Notification:
    REQUIRED_KEYS = []

    @abstractmethod
    def send_notification(self, **kwargs):
        pass

class EmailNotification(Notification):
    REQUIRED_KEYS = ["recipient", "email_title", "message"]

    def _validate_data(self, **kwargs):
        for key in self.REQUIRED_KEYS:
            input_value = kwargs.get(key, None)
            if input_value is None:
                print(f"Missing required key: {key}")
                return False
            elif input_value.strip() == "":
                print(f"this field cannot be empty: {key}")
                return False
        # validate the email address before sending the email
        try:
            print("Validating email address...")
            validate_email(kwargs["recipient"], check_deliverability=True)
            print("Email address is valid.")
        except EmailNotValidError:
            print(f"Invalid email address: {kwargs['recipient']}")
            return False

        return True

    def send_notification(self, **kwargs):
        # handle sending email notification
        # kwrgs will contain this dictionary - 
        """
        {
            "recipient": "email@example.com", 
            "email_title": "Hello, this is an email notification!", 
            "message": "This is the body of the email."
        }
        """ 
        is_valid = self._validate_data(**kwargs)
        if not is_valid:
            print("Failed to send email notification, validation failed.")
            return
        # logic to send email notification
        print(f"Sending email to {kwargs['recipient']} with title: {kwargs['email_title']} and message: {kwargs['message']}")

class SMSNotification(Notification):
    REQUIRED_KEYS = ["recipient", "message"]
    def send_notification(self, **kwargs):
        """
        kwrgs will contain this dictionary -
        {
            "recipient": "+1234567890", 
            "message": "This is an SMS notification."
        }
        """
        # handle sending SMS notification
        print(f"Sending SMS to {kwargs['recipient']} with message: {kwargs['message']}")

class PushNotification(Notification):
    def send_notification(self, **kwargs):
        """
        kwrgs will contain this dictionary -
        {
            "recipient": "<device_id>", 
            "message": "This is a push notification."
        }
        """
        # handle sending push notification
        print(f"Sending push notification to {kwargs['recipient']} with message: {kwargs['message']}")

class WhatsAppNotification(Notification):
    def send_notification(self, **kwargs):
        # handle sending WhatsApp notification
        # kwrgs will contain this dictionary - 
        """
        {
            "recipient": "+1234567890", 
            "message": "This is a WhatsApp notification."
        }
        """
        print(f"Sending WhatsApp message to {kwargs['recipient']} with message: {kwargs['message']}")

notification_manager = EmailNotification()
email_notification_data = {
    "recipient": "",
    "email_title": "Hello, this is an email notification!",
    "message": "This is the body of the email."
}
notification_manager.send_notification(**email_notification_data)

# home work (target date - 2026-04-05) 
"""
user factory design pattern, provide options to the user to choose the notification type, 
and then send the notification based on the user choice
"""

NotificationOptions = {
    "1": EmailNotification,
    "2": SMSNotification,
    "3": PushNotification,
    "4": WhatsAppNotification
}
NotificationOptionsNames = [
    "1. Email Notification", 
    "2. SMS Notification", 
    "3. Push Notification", 
    "4. WhatsApp Notification"
]

def get_notification_option(user_choice):
    if user_choice in NotificationOptions:
        return NotificationOptions[user_choice]()
    else:
        print("Invalid notification type selected.")
        return None

print("Notification system is ready to use, please choose your notification type:")
for option in NotificationOptionsNames:
    print(option)

user_choice = input("Enter the notification type: ")
notification_option = get_notification_option(user_choice)
notification_data = {
    "recipient": "aminul.islam@codebridgejapan.com",
    "email_title": "Hello, this is an email notification!",
    "message": "This is the body of the email."
}
if notification_option:
    notification_option.send_notification(**notification_data)

# home work (target date - 2026-04-05)
"""
complete the implementation of the notification system according to the discussion in the class
"""