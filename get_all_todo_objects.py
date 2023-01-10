from todo_object_service import db
from todo_object_service.common import create_success_response

def lambda_handler(event, context):
    todo_object_table = db.get_todo_app_table()
    response = todo_object_table.scan()
    return create_success_response(200, response['Items'])
