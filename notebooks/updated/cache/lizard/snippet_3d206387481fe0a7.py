def cmd_gimbal_mode(self, args):
    if len(args) != 1:
        print('usage: gimbal mode <GPS|MAVLink>')
        return
    if args[0].upper() == 'GPS':
        mode = mavutil.mavlink.MAV_MOUNT_MODE_GPS_POINT
    elif args[0].upper() == 'MAVLINK':
        mode = mavutil.mavlink.MAV_MOUNT_MODE_MAVLINK_TARGETING
    elif args[0].upper() == 'RC':
        mode = mavutil.mavlink.MAV_MOUNT_MODE_RC_TARGETING
    else:
        print('Unsupported mode %s' % args[0])
    self.master.mav.mount_configure_send(self.target_system, self.
        target_component, mode, 1, 1, 1)