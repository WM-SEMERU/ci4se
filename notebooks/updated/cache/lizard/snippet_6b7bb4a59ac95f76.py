def _stop_actions(self):
    Global.LOGGER.info('stopping actions')
    list(map(lambda x: x.stop(), self.actions))
    Global.LOGGER.info('actions stopped')