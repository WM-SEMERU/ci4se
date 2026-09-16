def serial_udb_extra_f13_encode(self, sue_week_no, sue_lat_origin,
    sue_lon_origin, sue_alt_origin):
    return MAVLink_serial_udb_extra_f13_message(sue_week_no, sue_lat_origin,
        sue_lon_origin, sue_alt_origin)