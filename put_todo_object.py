import json

from todo_object_service import db, fields
from todo_object_service.common import create_error_response, create_success_response

def lambda_handler(event, context):
    path_variables = event['pathParameters']
    todo_object_id = path_variables.get(fields.TODO_ID_PATH_VARIABLE)
    if not todo_object_id:
        return create_error_response(400, f"{fields.TODO_ID_PATH_VARIABLE} path variable must be set.")
    
    todo_object_table = db.get_todo_app_table()

    existing_item_response = todo_object_table.get_item(Key={fields.ID: todo_object_id})
    if not existing_item_response.get("Item"):
        return create_error_response(404, "The object with the provided ID could not be found.")

    existing_item = existing_item_response["Item"]

    body = json.loads(event['body'])

    if body.get(fields.TITLE):
        existing_item[fields.TITLE] = body[fields.TITLE]
    
    if body.get(fields.DESCRIPTION):
        existing_item[fields.DESCRIPTION] = body[fields.DESCRIPTION]

    todo_object_table.put_item(Item=existing_item)

    return create_success_response(200, existing_item)
