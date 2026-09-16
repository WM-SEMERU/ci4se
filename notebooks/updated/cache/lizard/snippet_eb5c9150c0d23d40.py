def _GetIgnoredDirs(self):
    goodlogging.Log.Info('CLEAR', 'Loading ignored directories from database:')
    goodlogging.Log.IncreaseIndent()
    ignoredDirs = self._db.GetIgnoredDirs()
    if ignoredDirs is None:
        goodlogging.Log.Info('CLEAR',
            'No ignored directories exist in database')
        ignoredDirs = self._UserUpdateIgnoredDirs()
    else:
        goodlogging.Log.Info('CLEAR',
            'Got ignored directories from database: {0}'.format(ignoredDirs))
    if self._archiveDir not in ignoredDirs:
        ignoredDirs.append(self._archiveDir)
    goodlogging.Log.Info('CLEAR', 'Using ignored directories: {0}'.format(
        ignoredDirs))
    goodlogging.Log.DecreaseIndent()
    return ignoredDirs