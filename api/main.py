from flask import Flask,jsonify

app = Flask(__name__)

trucks = [{"id": 1, "plate": "down", "type": "truck", "color": "black"},
          {"id": 2, "plate": "high", "type": "truck", "color": "red"},
          {"id": 3, "plate": "down", "type": "truck", "color": "white"},
          ]


@app.route('/')
def trucks_company():
    return "welcome truck company"

@app.route('/all')
def get_all_trucks():
    return jsonify(trucks)


@app.route('/truck/<int:truckId>')
def get_trucks_by_id(truckId):
    res = [truck for truck in trucks if truck.get("id") == truckId]
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)
