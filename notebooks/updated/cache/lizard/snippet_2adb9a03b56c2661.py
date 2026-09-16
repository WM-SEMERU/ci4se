def _handle_clear(self, load):
    log.trace('Clear payload received with command %s', load['cmd'])
    cmd = load['cmd']
    if cmd.startswith('__'):
        return False
    if self.opts['master_stats']:
        start = time.time()
    ret = getattr(self.clear_funcs, cmd)(load), {'fun': 'send_clear'}
    if self.opts['master_stats']:
        stats = salt.utils.event.update_stats(self.stats, start, load)
        self._post_stats(stats)
    return ret