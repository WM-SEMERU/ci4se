def wp_draw_callback(self, points):
    if len(points) < 3:
        return
    from MAVProxy.modules.lib import mp_util
    home = self.wploader.wp(0)
    self.wploader.clear()
    self.wploader.target_system = self.target_system
    self.wploader.target_component = self.target_component
    self.wploader.add(home)
    if self.get_default_frame(
        ) == mavutil.mavlink.MAV_FRAME_GLOBAL_TERRAIN_ALT:
        use_terrain = True
    else:
        use_terrain = False
    for p in points:
        self.wploader.add_latlonalt(p[0], p[1], self.settings.wpalt,
            terrain_alt=use_terrain)
    self.send_all_waypoints()