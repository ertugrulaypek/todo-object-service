from todo_object_service import db, fields
from todo_object_service.common import create_error_response, create_success_response

def lambda_handler(event, context):
    path_variables = event['pathParameters']
    todo_object_id = path_variables.get(fields.TODO_ID_PATH_VARIABLE)
    if not todo_object_id:
        return create_error_response(400, f"{fields.TODO_ID_PATH_VARIABLE} path variable must be set.")

    todo_object_table = db.get_todo_app_table()
    response = todo_object_table.get_item(Key={fields.ID: todo_object_id})
    if not response.get("Item"):
        return create_error_response(404, "The object with the provided ID could not be found.")

    return create_success_response(200, response['Item'])
