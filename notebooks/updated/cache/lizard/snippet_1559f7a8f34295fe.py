def cmd_gethome(self, args):
    self.master.mav.command_long_send(self.settings.target_system, 0,
        mavutil.mavlink.MAV_CMD_GET_HOME_POSITION, 0, 0, 0, 0, 0, 0, 0, 0)