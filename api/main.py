from flask import Flask, jsonify, request

app = Flask(__name__)

trucks = [{"id": 1, "plate": "down", "type": "truck", "color": "black"},
          {"id": 2, "plate": "high", "type": "truck", "color": "red"},
          {"id": 3, "plate": "down", "type": "truck", "color": "white"},
          ]
drivers = [{"id": 1, "name": "lucas", "last_name": "lopez", "number_license":123456 },
           {"id": 2, "name": "Peter", "last_name": "Pan", "number_license": 236547},
           {"id": 3, "name": "pepe", "last_name": "perez", "number_license":147852 }]


@app.route('/')
def trucks_company():
    return "welcome truck company"


@app.route('/truck/all')
def get_all_trucks():
    return jsonify(trucks)


@app.route('/truck/<int:truckId>')
def get_trucks_by_id(truckId):
    res = [truck for truck in trucks if truck.get("id") == truckId]
    return jsonify(res)


@app.route('/truck/save')
def create_truck():
    trucks.append(request.json)
    return jsonify(trucks)


@app.route('trucks/delete/<int:truckIs>')
def delete_truck(truckId):
    res = [truck for truck in trucks if truck.get("id") == truckId]
    trucks.remove(res)
    return jsonify(trucks)


@app.route('/drivers/all')
def get_all_driver():
    return jsonify(drivers)


@app.route('/drivers/<int:driverId>')
def get_driver_by_id(driverId):
    res = [driver for driver in drivers if driver.get("id") == driverId]
    return jsonify(res)


@app.route('/drivers/save')
def create_driver():
    drivers.append(request.json)
    return jsonify(drivers)


@app.route('drivers/delete/<int:driverId>')
def delete_driver(driverId):
    res = [driver for driver in drivers if driver.get("id") == driverId]
    drivers.remove(res)
    return jsonify(drivers)

@app.route('/drivers/<string:driver_name>')
def get_driver_by_id(driver_name):
    res = [driver for driver in drivers if driver.get("name") == driver_name]
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)
