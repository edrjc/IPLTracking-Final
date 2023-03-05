import requests

people_ms_url = 'http://localhost:8081/tracking/'
telemetry_profile_and_sensor_ms_url = 'http://localhost:8080/tracking/'
vehicle_ms_url = 'http://localhost:8083/tracking/'
data_ms_url = 'http://localhost:8084/tracking/'

'''
    Integration test (happy path):
    - create customer
    - create driver
     - - depends on customer
    - create sensor 
    - create telemetry profile
    - - depends on sensor
    - create vehicle
    - - depends on customer, telemetry profile, driver
    - create data
    - - GeoData
    - - - depends on vehicle
    - - TelemetryData
    - - - depends on vehicle, telemetry profile
'''


def create_entity(url, body, attr_id_name):
    response = requests.post(url, json=body)
    entity_id = response.json()[attr_id_name]
    return entity_id


# create customer
people_url = people_ms_url + 'customers'
body = {
    "mail": "people1@bar.com",
    "name": "People 1",
    "phone": "351111111111"
}
customer_id = create_entity(people_url, body, 'customer_id')
print('customer_id: ' + customer_id)

# create driver
driver_url = people_ms_url + 'drivers'
body = {
    "mail": "driver1@bar.com",
    "name": "Driver 1",
    "phone": "351222222222",
    "customerId": customer_id
}
driver_id = create_entity(driver_url, body, 'driver_id')
print('driver_id: ' + driver_id)

# create sensor
sensor_url = telemetry_profile_and_sensor_ms_url + 'sensors'
body = {
    "name": "ODO",
    "sensor_type": "ODOMETER",
    "minValue": 0.0,
    "maxValue": 555.0,
    "unit": "rpms"
}
sensor_id = create_entity(sensor_url, body, 'sensorId')
print('sensor_id: ' + sensor_id)

# create telemetry profile
telemetry_profile_url = telemetry_profile_and_sensor_ms_url + 'telemetryprofiles'
body = {
    "name": "People ODO",
    "sensors": [
        sensor_id
    ]
}
telemetryprofile_id = create_entity(telemetry_profile_url, body, 'telemetryprofileId')
print('telemetryprofile_id: ' + telemetryprofile_id)

# create vehicle
vehicle_url = vehicle_ms_url + 'vehicles'
body = {
    "customerId": customer_id,
    "driverId": driver_id,
    "telemetryProfileId": telemetryprofile_id,
    "plateNumber": "OO-11-OO",
    "vin": "OOO11",
    "color": "green"
}
vehicle_id = create_entity(vehicle_url, body, 'vehicleId')
print('vehicle_id: ' + vehicle_id)

# create geo data
data_url = data_ms_url + 'GeoData'
body = {
    "altimeter": "123",
    "latitude": "321",
    "longitude": "132",
    "vehicleId": vehicle_id
}
data_id = create_entity(data_url, body, 'data_id')
print('data_id (Geo): ' + data_id)

# create telemetry data
data_url = data_ms_url + 'TelemetryData'
body = {
    "sensor_type": "ODOMETER",
    "value": 55,
    "vehicleId": vehicle_id
}
data_id = create_entity(data_url, body, 'data_id')
print('data_id (Telemetry): ' + data_id)
