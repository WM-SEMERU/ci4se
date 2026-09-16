def simple_goto(self, location, airspeed=None, groundspeed=None):
    if isinstance(location, LocationGlobalRelative):
        frame = mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT
        alt = location.alt
    elif isinstance(location, LocationGlobal):
        frame = mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT
        if not self.home_location:
            self.commands.download()
            self.commands.wait_ready()
        alt = location.alt - self.home_location.alt
    else:
        raise ValueError(
            'Expecting location to be LocationGlobal or LocationGlobalRelative.'
            )
    self._master.mav.mission_item_send(0, 0, 0, frame, mavutil.mavlink.
        MAV_CMD_NAV_WAYPOINT, 2, 0, 0, 0, 0, 0, location.lat, location.lon, alt
        )
    if airspeed is not None:
        self.airspeed = airspeed
    if groundspeed is not None:
        self.groundspeed = groundspeed