def current_app(self):
    _activityRE = re.compile(
        'ACTIVITY (?P<package>[^/]+)/(?P<activity>[^/\\s]+) \\w+ pid=(?P<pid>\\d+)'
        )
    m = _activityRE.search(self.shell('dumpsys', 'activity', 'top'))
    if m:
        return dict(package=m.group('package'), activity=m.group('activity'
            ), pid=int(m.group('pid')))
    _focusedRE = re.compile(
        'mFocusedApp=.*ActivityRecord{\\w+ \\w+ (?P<package>.*)/(?P<activity>.*) .*'
        )
    m = _focusedRE.search(self.shell('dumpsys', 'window', 'windows'))
    if m:
        return dict(package=m.group('package'), activity=m.group('activity'))
    raise RuntimeError("Couldn't get focused app")