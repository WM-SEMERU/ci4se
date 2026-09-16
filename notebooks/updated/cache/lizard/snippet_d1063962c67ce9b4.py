def setChargingStationStop(self, vehID, stopID, duration=2 ** 31 - 1, until
    =-1, flags=tc.STOP_DEFAULT):
    self.setStop(vehID, stopID, duration=duration, until=until, flags=flags |
        tc.STOP_CHARGING_STATION)