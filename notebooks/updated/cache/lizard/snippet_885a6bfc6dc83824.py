def cmd_do_change_speed(self, args):
    if len(args) != 1:
        print('Usage: setspeed SPEED_VALUE')
        return
    if len(args) == 1:
        speed = float(args[0])
        print('SPEED %s' % str(speed))
        self.master.mav.command_long_send(self.settings.target_system,
            mavutil.mavlink.MAV_COMP_ID_SYSTEM_CONTROL, mavutil.mavlink.
            MAV_CMD_DO_CHANGE_SPEED, 0, 0, speed, 0, 0, 0, 0, 0)