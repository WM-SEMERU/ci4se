def setWidth(self, vehID, width):
    self._connection._sendDoubleCmd(tc.CMD_SET_VEHICLE_VARIABLE, tc.
        VAR_WIDTH, vehID, width)