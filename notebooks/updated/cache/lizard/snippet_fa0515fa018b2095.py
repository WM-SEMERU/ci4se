def uavionix_adsb_out_cfg_encode(self, ICAO, callsign, emitterType,
    aircraftSize, gpsOffsetLat, gpsOffsetLon, stallSpeed, rfSelect):
    return MAVLink_uavionix_adsb_out_cfg_message(ICAO, callsign,
        emitterType, aircraftSize, gpsOffsetLat, gpsOffsetLon, stallSpeed,
        rfSelect)