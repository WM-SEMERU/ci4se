def setPosition(self, poiID, x, y):
    self._connection._beginMessage(tc.CMD_SET_POI_VARIABLE, tc.VAR_POSITION,
        poiID, 1 + 8 + 8)
    self._connection._string += struct.pack('!Bdd', tc.POSITION_2D, x, y)
    self._connection._sendExact()