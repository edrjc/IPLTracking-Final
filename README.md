# IPL Tracking project

## Micro Services
- [IPLTracking-VehicleMS](https://github.com/edrjc/IPLTracking-VehicleMS)
- [IPLTracking-DataMS](https://github.com/edrjc/IPLTracking-DataMS)
- [IPLTracking-PeopleMS](https://github.com/edrjc/IPLTracking-PeopleMS)
- [IPLTracking-TelemetryMS](https://github.com/edrjc/IPLTracking-TelemetryMS)

## Integration test
All the Micro Services should be running for the test to work
```
python3 integration_test.py
```

### Integration test overview
```
    Test integration (happy path):
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
```

## Details
- Data MS (Python)
- - in SQLAlchemy, inheritance was implemented following the 'Joined Table Inheritance' approach [link #1](https://github.com/GitauHarrison/implementing-joined-table-inheritance-in-flask/tree/8cfff1c3925ee66be6fee72c18fa5887f35c34b0) [link #2](https://stackoverflow.com/questions/1337095/sqlalchemy-inheritance)
- - in Swagger, inheritance was implemented using composition [link](https://swagger.io/docs/specification/data-models/inheritance-and-polymorphism/)
- - if you are using python v3.10+, the last version of the python-dateutil package should be used
- - update doesn't allow updating vehicle_id, if needed data should be deleted

- Vehicle MS (Java)
- - it should not be possible to create a vehicle with the same vin and/or plate number
- - it should not be possible to update vin and/or plate number
