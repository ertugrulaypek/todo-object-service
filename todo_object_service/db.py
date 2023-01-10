import boto3

from botocore.config import Config
from typing import Final

_DB_NAME: Final = 'dynamodb'
_DB_TABLE_NAME: Final = 'todo-app'

def get_todo_app_table():
    dynamodb = boto3.resource(_DB_NAME)
    return dynamodb.Table(_DB_TABLE_NAME)
