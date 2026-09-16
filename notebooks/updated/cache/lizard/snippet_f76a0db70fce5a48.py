def setMaxSpeedLat(self, vehID, speed):
    self._connection._sendDoubleCmd(tc.CMD_SET_VEHICLE_VARIABLE, tc.
        VAR_MAXSPEED_LAT, vehID, speed)