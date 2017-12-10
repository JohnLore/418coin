from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from json import dumps
from flask_jsonpify import jsonify

from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy(app)
api = Api(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(40))
    timestamp = db.Column(db.String(40))

    def __init__(self, location):
        self.location = location
        self.timestamp = str(datetime.now())

    def __repr__(self):
        return '<Entry %r>' % self.location

# Create the table 
db.create_all()

class Locations(Resource):
    def get(self):
        entries = Entry.query.all()
        print("helloGet\n");
        result = {'data': [(entries.keys() ,i) for i in entries]}
        return jsonify(result)
    def post(self):
        print("helloPost1\n");
        print("entry %s\n", str(request))
        entry = Entry(request.json['location'])
        print("helloPost2\n");
        db.session.add(entry)
        print("helloPost3\n");
        db.session.commit()
        print("helloPost4\n");
        entries = Entry.query.all()
        print("helloPost5\n");
        result = {'data': [(entries.keys() ,i) for i in entries]}
        print("helloPost6\n");
        return jsonify(result)
        
api.add_resource(Locations, '/locations') # Route_3

@app.route('/')
def hello():
    return "Testing.. Success!"


if __name__ == '__main__':
     app.run(port='5000', host='0.0.0.0')