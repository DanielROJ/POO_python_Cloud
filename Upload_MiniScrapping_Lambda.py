from bs4 import  BeautifulSoup
import re
import json
import boto3 
from urllib import parse
import uuid
import datetime

def lambda_handler(event,context):
    ##Create client S3
    s3 = boto3.client('s3')
    ##Extract atributes
    bucket = event["Records"][0]["s3"]["bucket"]["name"];
    nombreArchivo = parse.unquote(event["Records"][0]["s3"]["object"]["key"]);
    ##Donwload File to TMṔ
    s3.download_file(bucket,nombreArchivo,'/tmp/{}'.format('tmp.html'))
    
    date = datetime.date.today()
    
    content = open('/tmp/tmp.html','r')
    soup = BeautifulSoup(content,'html.parser')
    text = soup.find('body').string
    text2 = text.split('\n')
    
    arr =[]
    for x in text2:
        arr.extend(x.split(' '))
        pass
    
    fol = open('/tmp/atom.txt','w')
    for x in arr:
        fol.write(x+'\n')
        fol.flush()
        pass
    fol.close()
    nombreArchivo = nombreArchivo.replace('.html','')
    bucket2 = 'zteh1'
    ##Uploa file to other bucket
    s3.upload_file('/tmp/atom.txt',bucket2,'new_{}_{}.txt'.format(nombreArchivo,date))

    return;

