def setStop(self, vehID, edgeID, pos=1.0, laneIndex=0, duration=2 ** 31 - 1,
    flags=tc.STOP_DEFAULT, startPos=tc.INVALID_DOUBLE_VALUE, until=-1):
    self._connection._beginMessage(tc.CMD_SET_VEHICLE_VARIABLE, tc.CMD_STOP,
        vehID, 1 + 4 + 1 + 4 + len(edgeID) + 1 + 8 + 1 + 1 + 1 + 4 + 1 + 1 +
        1 + 8 + 1 + 4)
    self._connection._string += struct.pack('!Bi', tc.TYPE_COMPOUND, 7)
    self._connection._packString(edgeID)
    self._connection._string += struct.pack('!BdBBBiBB', tc.TYPE_DOUBLE,
        pos, tc.TYPE_BYTE, laneIndex, tc.TYPE_INTEGER, duration, tc.
        TYPE_BYTE, flags)
    self._connection._string += struct.pack('!BdBi', tc.TYPE_DOUBLE,
        startPos, tc.TYPE_INTEGER, until)
    self._connection._sendExact()