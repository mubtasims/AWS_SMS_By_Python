import boto3
client= boto3.client ('sns', 'us-east-1')
client.publish(PhoneNumber= '+1234567890', Message= '#BlackLivesMatter')