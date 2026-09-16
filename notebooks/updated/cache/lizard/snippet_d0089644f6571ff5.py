def setShapeClass(self, typeID, clazz):
    self._connection._sendStringCmd(tc.CMD_SET_VEHICLETYPE_VARIABLE, tc.
        VAR_SHAPECLASS, typeID, clazz)