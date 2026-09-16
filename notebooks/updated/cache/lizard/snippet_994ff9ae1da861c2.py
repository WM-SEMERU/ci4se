def whisper_lock_writes(self, cluster='main'):
    if not self.config.has_section(cluster):
        raise SystemExit("Cluster '%s' not defined in %s" % (cluster, self.
            config_file))
    try:
        return bool(self.config.get(cluster, 'whisper_lock_writes'))
    except NoOptionError:
        return False