def setImperfection(self, typeID, imperfection):
    self._connection._sendDoubleCmd(tc.CMD_SET_VEHICLETYPE_VARIABLE, tc.
        VAR_IMPERFECTION, typeID, imperfection)