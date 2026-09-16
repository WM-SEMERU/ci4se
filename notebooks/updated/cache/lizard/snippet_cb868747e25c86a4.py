def setLength(self, vehID, length):
    self._connection._sendDoubleCmd(tc.CMD_SET_VEHICLE_VARIABLE, tc.
        VAR_LENGTH, vehID, length)