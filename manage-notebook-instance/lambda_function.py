import json
import boto3
import logging
from datetime import datetime as dt

def lambda_handler(event, context):
    client = boto3.client('sagemaker')
    
    if dt.now().hour + 1 ==8: #This is 8am WAT. You can adjust to your preference
        client.start_notebook_instance(NotebookInstanceName='check-notebook')
        print(dt.now().hour + 1)
    
    if dt.now().hour + 1 ==19: #This is 7pm WAT. You can adjust to your preference
        response_nb_list = client.list_notebook_instances(StatusEquals= 'InService') #retrieves a list of notebooks that are running
        for nb in response_nb_list['NotebookInstances']:
            client.stop_notebook_instance(NotebookInstanceName=nb['NotebookInstanceName']) #stop all notebooks in service at exactly 7pm
        
    
    return {
        'statusCode': 200,
        'body': json.dumps('Notebook started successfully')
    }
