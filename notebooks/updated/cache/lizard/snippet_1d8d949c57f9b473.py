def update_recurrent_works_tick(self, conf):
    for key in self.recurrent_works:
        name, fun, _ = self.recurrent_works[key]
        if isinstance(conf, dict):
            new_tick = conf.get('tick_%s' % name, None)
        else:
            new_tick = getattr(conf, 'tick_%s' % name, None)
        if new_tick is not None:
            logger.debug(
                'Requesting to change the default tick to %d for the action %s'
                , int(new_tick), name)
        else:
            continue
        try:
            new_tick = int(new_tick)
            logger.info('Changing the default tick to %d for the action %s',
                new_tick, name)
            self.recurrent_works[key] = name, fun, new_tick
        except ValueError:
            logger.warning("Changing the default tick for '%s' to '%s' failed!"
                , new_tick, name)