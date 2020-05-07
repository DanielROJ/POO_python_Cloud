import json
import boto3
from urllib import parse

def lambda_handler(event, context):
    # TODO implement
     
    ##Create client S3, Rekognition, DynamoDB
    s3 = boto3.client('s3')
    rk = boto3.client('rekognition')
    dy = boto3.client('dynamodb')
    ##Extract atributes
    bucket = event["Records"][0]["s3"]["bucket"]["name"];
    nombreArchivo = parse.unquote(event["Records"][0]["s3"]["object"]["key"]);
    ##Donwload File to TMṔ
    responseRK = rk.detect_labels(
            Image={
                'S3Object': {
                            'Bucket': bucket,
                             'Name': nombreArchivo,
                 }
            },
            MaxLabels=10
        )
    
    nombreOBJ = responseRK['Labels'][0]['Name']
    url_file = 'https://rekog123.s3.amazonaws.com/'+nombreArchivo    
    responseDY = dy.put_item(
    TableName='taller',
    Item={
        'nameId':{
           'S': nombreOBJ
        },
        'url_file':{
            'S': url_file
        }
    })
    
    return {
        'statusCode': 200,
        'body': json.dumps('FUSION REKOGNIGITON, S3 AND DYNAMO DB !!!!COMPLETE!!!')
    }
