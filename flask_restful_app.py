from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import os


app = Flask(__name__)
api = Api(app)

class example(Resource):
    def get(self,argument1):
        data = "You have submitted GET: " + str(argument1)
        return jsonify(data) #return data will 
    def post(self,argument1):
        data = "You have submitted POST: " + str(argument1)
        return jsonify(data) #return data will 
api.add_resource(example, '/example/url/<string:argument1>')
 
# This will GET request to http://localhost/example/url/argument1
# argument1 is dynamic and can return different 


if __name__ == '__main__':
    # run flask server on this machine's local host
    # works with cloud servers
    # change file name to flask_app.py before deploying on cloud
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8081)), use_reloader=False, debug=True)