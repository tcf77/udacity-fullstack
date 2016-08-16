#from twilio.rest import TwilioRestClient
from twilio import rest

account_sid = "AC97f5d22973d6e670f6ced3bbff36184a" # Your Account SID from www.twilio.com/console
auth_token  = "ef3c31676eccfbfb133b79330816fb93"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="My name is Bond, James Blonde",
    to="+13477094164",    # Replace with your phone number
    from_="+19143689459") # Replace with your Twilio number

print(message.sid)
