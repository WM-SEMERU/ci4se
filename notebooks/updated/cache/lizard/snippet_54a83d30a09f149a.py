def roster(opts, runner=None, utils=None, whitelist=None):
    return LazyLoader(_module_dirs(opts, 'roster'), opts, tag='roster',
        whitelist=whitelist, pack={'__runner__': runner, '__utils__': utils})