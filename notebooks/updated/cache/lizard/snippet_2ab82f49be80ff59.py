def addFull(self, vehID, routeID, typeID='DEFAULT_VEHTYPE', depart=None,
    departLane='first', departPos='base', departSpeed='0', arrivalLane=
    'current', arrivalPos='max', arrivalSpeed='current', fromTaz='', toTaz=
    '', line='', personCapacity=0, personNumber=0):
    messageString = struct.pack('!Bi', tc.TYPE_COMPOUND, 14)
    if depart is None:
        depart = str(self._connection.simulation.getCurrentTime() / 1000.0)
    for val in (routeID, typeID, depart, departLane, departPos, departSpeed,
        arrivalLane, arrivalPos, arrivalSpeed, fromTaz, toTaz, line):
        messageString += struct.pack('!Bi', tc.TYPE_STRING, len(val)) + str(val
            ).encode('latin1')
    messageString += struct.pack('!Bi', tc.TYPE_INTEGER, personCapacity)
    messageString += struct.pack('!Bi', tc.TYPE_INTEGER, personNumber)
    self._connection._beginMessage(tc.CMD_SET_VEHICLE_VARIABLE, tc.ADD_FULL,
        vehID, len(messageString))
    self._connection._string += messageString
    self._connection._sendExact()