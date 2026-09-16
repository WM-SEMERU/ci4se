def wait_for_device_ready(self, timeout=None, wait_polling_interval=None,
    after_first=None):
    if timeout is None:
        timeout = self._timeout
    if wait_polling_interval is None:
        wait_polling_interval = self._wait_polling_interval
    self._logger.info('Waiting for device to become ready')
    profiles = self.get_profiles()
    assert len(profiles) == 1
    profile_dir = profiles.itervalues().next()
    prefs_file = posixpath.normpath(profile_dir + '/prefs.js')
    current_date = int(self.shell_output('date +"%s"'))
    set_date = current_date - (365 * 24 * 3600 + 24 * 3600 + 3600 + 60 + 1)
    try:
        self.shell_output('touch -t %i %s' % (set_date, prefs_file))
    except adb.ADBError:
        set_date = datetime.datetime.fromtimestamp(set_date)
        self.shell_output('touch -t %s %s' % (set_date.strftime(
            '%Y%m%d.%H%M%S'), prefs_file))

    def prefs_modified():
        times = [None, None]

        def inner():
            try:
                listing = self.shell_output('ls -l %s' % prefs_file)
                mode, user, group, size, date, time, name = listing.split(None,
                    6)
                mtime = '%s %s' % (date, time)
            except:
                return False
            if times[0] is None:
                times[0] = mtime
            else:
                times[1] = mtime
                if times[1] != times[0]:
                    return True
            return False
        return inner
    poll_wait(prefs_modified(), timeout=timeout, polling_interval=
        wait_polling_interval, after_first=after_first)