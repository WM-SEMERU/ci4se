def launch_browser(self, profile, timeout=30):
    self.profile = profile
    self._start_from_profile_path(self.profile.path)
    self._wait_until_connectable(timeout=timeout)