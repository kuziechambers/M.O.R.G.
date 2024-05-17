import os
from twilio.rest import Client


TWILIO_ACCOUNT_ID = os.getenv("TWILIO_ACCOUNT_ID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(TWILIO_ACCOUNT_ID, TWILIO_AUTH_TOKEN)


def send_text(body):

    try:
        client.messages \
            .create(
                 messaging_service_sid='MG604a957ab382c1215ad46d9444c5101c',
                 body=str(body),
                 to='+19402311617'
             )
    except:
        print("Message wasn't sent")
