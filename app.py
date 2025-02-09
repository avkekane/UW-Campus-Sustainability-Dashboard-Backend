from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# returns a list of all building names
@app.route('/api/building-names', methods = ['GET'])
def getBuildingNames():
    data={}
    return jsonify(data), 200

# returns details for a specific building
@app.route('/api/building/<id>', methods = ['GET'])
def getBuildingDetails(id):
    induvisual_building_data = {}
    return jsonify(induvisual_building_data),200

# returns university information
@app.route('/api/university', methods = ['GET'])
def getUniversityInfo():
    uni_info={}
    return jsonfiy(uni_info),200

# if __name__ == '__main__':
#     app.run(debug=True)
