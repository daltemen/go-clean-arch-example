from flask_api import FlaskAPI, status
from flask import request

from trips.repository.mongo_repo import MongoDataSource
from trips.trips_management import TripsManagement

app = FlaskAPI(__name__)

mongo_data_source = MongoDataSource()
trips = TripsManagement(mongo_data_source)


@app.route("/")
def index():
    return "Hi Mi Aguila"


@app.route("/health")
def health():
    return "Mi Aguila Health"


@app.route("/trips/counts", methods=["GET"])
def trips_counts():
    city = request.args.get("city")
    if city:
        count = trips.count_trips_by_city(city)
    else:
        count = trips.count_trips()
    return {"count": count}, status.HTTP_200_OK


@app.route("/trips", methods=["POST", "PUT"])
def trips_create_update():
    ok = False
    if request.method == "POST":
        payload_creation = request.get_json()
        ok = trips.create_trip(payload_creation)
        return {"ok": ok}, status.HTTP_201_CREATED
    elif request.method == "PUT":
        payload_creation = request.get_json()
        ok = trips.update_trip(payload_creation)
    return {"ok": ok}, status.HTTP_200_OK


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)
