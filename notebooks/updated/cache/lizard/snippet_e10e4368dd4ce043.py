def mark_dead(self, connection, now=None):
    now = now if now else time.time()
    try:
        self.connections.remove(connection)
    except ValueError:
        return
    else:
        dead_count = self.dead_count.get(connection, 0) + 1
        self.dead_count[connection] = dead_count
        timeout = self.dead_timeout * 2 ** min(dead_count - 1, self.
            timeout_cutoff)
        self.dead.put((now + timeout, connection))
        logger.warning(
            'Connection %r has failed for %i times in a row, putting on %i second timeout.'
            , connection, dead_count, timeout)