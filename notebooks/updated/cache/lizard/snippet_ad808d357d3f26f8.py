def set_mode_auto(self):
    if self.mavlink10():
        self.mav.command_long_send(self.target_system, self.
            target_component, mavlink.MAV_CMD_MISSION_START, 0, 0, 0, 0, 0,
            0, 0, 0)
    else:
        MAV_ACTION_SET_AUTO = 13
        self.mav.action_send(self.target_system, self.target_component,
            MAV_ACTION_SET_AUTO)