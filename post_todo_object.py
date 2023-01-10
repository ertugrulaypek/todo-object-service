import boto3
import json
import uuid

from todo_object_service.common import create_error_response, create_success_response
from todo_object_service import db, fields

def lambda_handler(event, context):
    body = json.loads(event['body'])
    if not body.get(fields.TITLE) or not body.get(fields.DESCRIPTION):
        return create_error_response(400, f"{fields.TITLE} and {fields.DESCRIPTION} fields must be defined!")
    
    todo_object_table = db.get_todo_app_table()
    object_id = str(uuid.uuid4())
    new_todo_object = {
        fields.ID: object_id,
        fields.TITLE: body[fields.TITLE],
        fields.DESCRIPTION: body[fields.DESCRIPTION]
    }
    todo_object_table.put_item(Item=new_todo_object)
    return create_success_response(201, new_todo_object)

