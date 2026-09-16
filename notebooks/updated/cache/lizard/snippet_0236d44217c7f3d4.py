def send_calibrate_magnetometer(self):
    if self._autopilot_type == mavutil.mavlink.MAV_AUTOPILOT_ARDUPILOTMEGA:
        calibration_command = self.message_factory.command_long_encode(self
            ._handler.target_system, 0, mavutil.mavlink.
            MAV_CMD_DO_START_MAG_CAL, 0, 0, 1, 1, 0, 0, 0, 0)
    else:
        calibration_command = self.message_factory.command_long_encode(self
            ._handler.target_system, 0, mavutil.mavlink.
            MAV_CMD_PREFLIGHT_CALIBRATION, 0, 0, 1, 0, 0, 0, 0, 0)
    self.send_mavlink(calibration_command)