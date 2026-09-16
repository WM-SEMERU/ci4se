def export(self, input_stats=None):
    input_stats = input_stats or {}
    for e in self._exports:
        logger.debug('Export stats using the %s module' % e)
        thread = threading.Thread(target=self._exports[e].update, args=(
            input_stats,))
        thread.start()