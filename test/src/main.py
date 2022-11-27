from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        file_loc = "/home/mnist_model/fake-data.txt"

        with open(file_loc, 'w') as file:
            file.write(" - Content written to file!!")

        f = open(file_loc, "r")
        str = f.read()
        # str += " - SECOND APP!!!"
        return str

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')