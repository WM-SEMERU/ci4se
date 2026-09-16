def createLists(self):
    self.beforeAssemblyList = {'Confirm batteries charged': 2,
        'No physical damage to airframe': 2,
        'All electronics present and connected': 2, 'Bottle loaded': 2,
        'Ground station operational': 2}
    self.beforeEngineList = {'Avionics Power ON': 2, 'Pixhawk Booted': 0,
        'Odroid Booted': 2, 'Cameras calibrated and capturing': 2,
        'GPS lock': 0, 'Airspeed check': 2, 'Barometer check': 2,
        'Compass check': 2, 'Flight mode MANUAL': 0, 'Avionics Power': 0,
        'Servo Power': 0, 'IMU Check': 0, 'Aircraft Params Loaded': 2,
        'Waypoints Loaded': 0, 'Servo and clevis check': 2,
        'Geofence loaded': 2, 'Ignition circuit and battery check': 2,
        'Check stabilisation in FBWA mode': 2}
    self.beforeTakeoffList = {'Engine throttle responsive': 2,
        'Runway clear': 2, 'Radio links > 6db margin': 0,
        'Antenna tracker check': 2, 'GCS stable': 2}
    self.beforeCruiseList = {'Airspeed > 10 m/s': 0, 'Altitude > 30 m': 0,
        '< 100 degrees to 1st Waypoint': 2,
        'Airspeed and climb rate nominal': 2}
    self.bottleDropList = {'Joe found': 2, 'Joe waypoint laid in': 2,
        '< 100m to Joe waypoint': 2, 'Bottle drop mechanism activated': 2}
    self.beforeLandingList = {'Runway clear': 2, 'APM set to FBWA mode': 2,
        '< 100m from airfield home': 2}
    self.beforeShutdownList = {'Taxi to parking': 2, 'Engine cutoff': 2,
        'Data downloaded': 2, 'Ignition power off': 2, 'Avionics power off': 2}