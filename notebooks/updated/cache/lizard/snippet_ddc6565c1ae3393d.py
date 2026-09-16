def setVehicleClass(self, vehID, clazz):
    self._connection._sendStringCmd(tc.CMD_SET_VEHICLE_VARIABLE, tc.
        VAR_VEHICLECLASS, vehID, clazz)