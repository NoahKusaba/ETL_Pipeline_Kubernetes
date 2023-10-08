from prefect import flow
import requests
from boto3 import client
import os
from dotenv import load_dotenv
load_dotenv()



@flow(name ="Get_Activity")
def main():
    activity_suggestion = requests.get("https://www.boredapi.com/api/activity/").json()['activity']
    send_email(activity_suggestion)

def send_email(activity):
    id = os.getenv('ID')
    key = os.getenv('KEY')
    print(id)
    email_client = client('ses', region_name='us-east-1', aws_access_key_id= id, aws_secret_access_key= key)
    response = email_client.send_email(
    Destination={ 'ToAddresses': ['nkusaba@bearcognition.com'] },
    Message={
        'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': activity,
            }
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': f'Noah-Kusaba - Activity Suggestion',
        },
    },
    Source='nkusaba@bearcognition.com'
    )

main()
