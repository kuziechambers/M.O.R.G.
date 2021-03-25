import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC145373d940dc7db98d51d95f0e012e49'
auth_token = 'b90e491eda918a4565101c38573f9fd9'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         messaging_service_sid='MG604a957ab382c1215ad46d9444c5101c',
         body='body',
         to='+19402311617'
     )

print(message.sid)