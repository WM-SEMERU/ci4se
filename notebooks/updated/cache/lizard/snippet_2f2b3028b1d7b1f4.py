def run(self):
    try:
        logger.info('running work unit {0}'.format(self.key))
        run_function = getattr(self.module, self.spec['run_function'])
        ret_val = run_function(self)
        self.update()
        logger.info('completed work unit {0}'.format(self.key))
        return ret_val
    except LostLease:
        logger.warning('work unit {0} timed out'.format(self.key))
        raise
    except Exception:
        logger.error('work unit {0} failed'.format(self.key), exc_info=True)
        raise