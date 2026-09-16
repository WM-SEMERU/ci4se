def stop_app(self):
    try:
        if self._conn:
            try:
                self.closeSl4aSession()
            except:
                self.log.exception('Failed to gracefully shut down %s.',
                    self.app_name)
            self.disconnect()
            self.stop_event_dispatcher()
        self._adb.shell('am force-stop com.googlecode.android_scripting')
    finally:
        self.clear_host_port()