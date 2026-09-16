def get_clamav_conf(filename):
    if os.path.isfile(filename):
        return ClamavConfig(filename)
    log.warn(LOG_PLUGIN, 'No ClamAV config file found at %r.', filename)