'''
Create Role Based Access Control Enabled BE with following functions

Create 2 Object Models with distinct API Routes
1.    1st Object can be-Organisation, College, Community Etc. Etc.
      1. Create 2 Objects of this type
2.    2nd Object can be-Employee, Books, Events Etc. Etc.
      1. Create Relationship of this Objects to above created Object 1
Store & Manage these Object Model on MongoDB Instance
Secure this REST API using JWT authentication
Perform Search Functionality among the data
Perform CRUD(POST, GET, PUT, PATCH, and DELETE) Operation on this API using Postman
Assign RBAC with following Rights
1.    Role 1 Should have Create & Read Permissions
2.    Role 2 Should have Create, Read & Update Permissions
3.    Role 2 Should have Create, Read, Update & Deleted Permissions
Include 5 TestCases
'''
from flask import Flask, request
from flask_restful import Api, Resource
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/testdb'
#app.config['MONGO_URI'] = 'mongodb+srv://pellurideepthi:deepthi@cluster0.mongodb.net/admin'
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
#app.config['JWT_SECRET_KEY'] = '73df4ccff955f301672f26c91ece1985bb05bfb9ac9b76866a9d05897d889d54'
mongo = PyMongo(app)
jwt = JWTManager(app)

# Define the MongoDB collections
org_collection = mongo.db.organizations
emp_collection = mongo.db.employees

# Object 1: Organization, College, Community, etc.
class OrganizationResource(Resource):
    @jwt_required()
    def get(self, org_id):
        # Implement your read logic here
        return {'message': 'Read organization with id {}'.format(org_id)}

    @jwt_required()
    def post(self):
        # Implement your create logic here
        return {'message': 'Organization created successfully'}

# Object 2: Employee, Books, Events, etc.
class EmployeeResource(Resource):
    @jwt_required()
    def get(self, emp_id):
        # Implement your read logic here
        return {'message': 'Read employee with id {}'.format(emp_id)}

    @jwt_required()
    def put(self, emp_id):
        # Implement your update logic here
        return {'message': 'Employee updated successfully'}

    @jwt_required()
    def delete(self, emp_id):
        # Implement your delete logic here
        return {'message': 'Employee deleted successfully'}

# TestCases
def test_organization_creation():
    # Implement your test case here
    pass

# Add other test cases...

# API routes
api.add_resource(OrganizationResource, '/organization', '/organization/<string:org_id>')
api.add_resource(EmployeeResource, '/employee', '/employee/<string:emp_id>')

if __name__ == '__main__':
    app.run(debug=True)
