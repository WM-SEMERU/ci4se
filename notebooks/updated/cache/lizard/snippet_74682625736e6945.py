def dump_state(self):
    superstate = super(ReferenceController, self).dump_state()
    superstate.update({'state_name': self.STATE_NAME, 'state_version': self
        .STATE_VERSION, 'app_info': self.app_info, 'os_info': self.os_info,
        'remote_bridge': self.remote_bridge.dump(), 'tile_manager': self.
        tile_manager.dump(), 'config_database': self.config_database.dump(),
        'sensor_log': self.sensor_log.dump()})
    return superstate