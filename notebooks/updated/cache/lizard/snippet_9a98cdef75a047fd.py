def get_daemon_stats(self, details=False):
    logger.debug('Get daemon statistics for %s, %s %s', self.name, self.
        alive, self.reachable)
    return self.con.get('stats%s' % ('?details=1' if details else ''))