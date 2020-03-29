import json
import boto3 
from urllib import parse
import uuid

##Daniel Rojas
##Ingenieria de sistemas y telecomunicaciones punto1
def lambda_handler(event, context):
    
    ##Create client S3
    s3 = boto3.client('s3')
    ##Extract atributes
    bucket = event["Records"][0]["s3"]["bucket"]["name"];
    nombreArchivo = parse.unquote(event["Records"][0]["s3"]["object"]["key"]);
    ##Donwload File to TMṔ
    print(nombreArchivo)
    print(bucket)
    s3.download_file(bucket,nombreArchivo,'/tmp/{}'.format('tmp.txt'))
    ##Open and read file tmp
    fil = open('/tmp/tmp.txt','r')
    data = fil.read()
    fil.flush()
    arr =data.split('\n')
    arr.pop(0)
    arr.pop(0)
    fil.close()
    ## Open and write File tmp
    fol = open('/tmp/tmp.txt','w')
    for x in arr:
        fol.write(x)
        fol.flush()
        pass
    fol.close()
    bucket2 = 'zte98'
    ##Uploa file to other bucket
    s3.upload_file('/tmp/tmp.txt',bucket2,'new_{}'.format(nombreArchivo))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
