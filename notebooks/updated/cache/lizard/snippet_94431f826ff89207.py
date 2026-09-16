def setSpeedDeviation(self, typeID, deviation):
    self._connection._sendDoubleCmd(tc.CMD_SET_VEHICLETYPE_VARIABLE, tc.
        VAR_SPEED_DEVIATION, typeID, deviation)