# TODO Object Backend Service

**Keywords**: *Python, AWS Lambda, AWS API Gateway, DynamoDB* 

## Introduction

This project implements API specification in *openapi.yml* file. The project aims to have CRUD operations to interact with TODO objects. A TODO object includes a title, description and an ID.

Since the expected load is low and rare, it is deployed to AWS using API Gateway and Lambda. Each endpoint can be considered as a separate AWS Lambda function. Hence, there are five functions for five endpoints. As the DB, AWS DynamoDB is used.

## Testing deployed instance

A deployed instance running on AWS can be found [here](https://uu8ghnsh1m.execute-api.us-east-2.amazonaws.com/test). One can upload the openapi.yml file to https://editor.swagger.io/ and interact with the instance.

## Deploying from scratch

Following the official docs ([link](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html)), one can deploy the functions to AWS Lambda by uploading the *.zip* files under *dist* directory. After the deployment, one can test the endpoints from AWS API Gateway. In order to get it working with Swagger editor, CORS should be enabled. It can be achieved following the steps described in [official AWS docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html).