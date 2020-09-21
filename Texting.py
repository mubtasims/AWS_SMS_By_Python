import boto3
client= boto3.client ('sns', 'us-east-1')
client.publish(PhoneNumber= '13476573589', Message= '#BlackLivesMatter')