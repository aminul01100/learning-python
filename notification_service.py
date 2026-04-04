"""
there will be three options to send out notifications to  the user-
1. Email
2. SMS
3. Push Notification
"""
from abc import ABC, abstractmethod


class Notification:
    @abstractmethod
    def send_notification(self, **kwargs):
        pass

class EmailNotification(Notification):
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
        print(f"Sending email to {kwargs['recipient']} with title: {kwargs['email_title']} and message: {kwargs['message']}")

class SMSNotification(Notification):
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


# home work (target date - 2026-04-05) 
"""
user factory design pattern, provide options to the user to choose the notification type, 
and then send the notification based on the user choice
"""