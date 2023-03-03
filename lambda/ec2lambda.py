import json
import os
import subprocess
import boto3
import logging
import urllib3

slack_url = os.environ['slack_url']
teams_url = os.environ['teams_url']

def lambda_handler(event, context):
    print("@@@@")
    print(event)
    eventtype = event['detail']['eventName']
    account= event['account']
    region = event['region']
    d = event['detail']['responseElements']['instancesSet']['items']
    instanceid = d[0]['instanceId']
    #keyname= d[0]['keyName']
    intsttype =d[0]['instanceType']
    client = boto3.client('cloudtrail')
    client1 = boto3.client('sns')
    response = client.lookup_events(
    LookupAttributes=[
        {
            'AttributeKey': 'ResourceName',
            'AttributeValue': instanceid
        },
    ],
    MaxResults=2)
    test=response['Events']
    st="".join(str(x) for x in test)
    if 'RunInstances' in st:
        user=st.split("Resources")[1]
        finalname=user.split(",")[-2]
        name = finalname.split(":")[1]
        #message = "Ec2 has been Launched. \n" + "Incident: "+str(eventtype) 
        message = "Ec2 has been Launched. \n" + "Incident: "+str(eventtype) + "\n" + "Account: " + account + "\n" + 'Instanceid: ' + instanceid+ "\n" + 'Region: ' + str(region) + "\n" + 'Instancetype: ' + str(intsttype)+ '\n' + "User: "+ str(name)
        post_to_slack(message)
        
    
        
def post_to_slack(message):
    webhook_url = slack_url
    #log.info(str(webhook_url))
    teams_webhook_url = teams_url
    #log.info(str(teams_webhook_url))
    slack_data = {'text': message}
    http = urllib3.PoolManager()
    headers={'Content-Type': 'application/json'}
    encoded_data = json.dumps(slack_data).encode('utf-8')
    response = http.request('POST',webhook_url,body=encoded_data,headers=headers)
    #log.info('response is :'+str(response))
    response1 = http.request('POST',teams_webhook_url,body=encoded_data,headers=headers)
    #og.info('response-1 is :'+str(response1))
    #return True

