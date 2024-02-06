from flask import jsonify
from flask_restful import Api, Resource

api = Api(app)

class ContainerScan(Resource):
    def get(self):



api.add_resource(ContainerScan, '/container-scanning')
