import json
import boto3
def lambda_handler(event, context):
    received_data = get_data()
    bucket_name = "eran-lambda-001"
    file_name = "some-data03.json"
    s3_path = file_name
    s3 = boto3.resource("s3") 
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=(bytes(json.dumps(received_data).encode('UTF-8'))))
    return {'msg': 'Done' }
def get_data():
    data = {}
    data['people'] = []
    data['people'].append({'name': 'Scott','website': 'stackabuse.com','from': 'Nebraska'})
    data['people'].append({'name': 'Larry','website': 'google.com','from': 'Michigan'})
    data['people'].append({'name': 'Tim','website': 'apple.com','from': 'Alabama'})
    return data
