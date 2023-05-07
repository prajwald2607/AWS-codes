import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    eventName = event['Records'][0]['eventName']
    eventTime = event['Records'][0]['eventTime']
    sourceIPAddress = event['Records'][0]['requestParameters']['sourceIPAddress']
    buckeName = event['Records'][0]['s3']['bucket']['name']
    objectName = event['Records'][0]['s3']['object']['key']
    
    print(eventName)
    print(eventTime)
    
    dynamodb = boto3.resource('dynamodb') 
    #table name
    table = dynamodb.Table('lab-20-3-23-table')
    
    
    response = table.put_item(
       Item={
            'eventTime':eventTime,
            'eventName':eventName,
            'sourceIPAddress':sourceIPAddress,
            'buckeName':buckeName,
            'objectName':objectName
        }
    )
    print(response)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
