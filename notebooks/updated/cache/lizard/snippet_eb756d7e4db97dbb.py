def start(self):
    logger.info('Starting client.')
    self.dispatcher_greenlets = []
    for _, entry in self.config['baits'].items():
        for b in clientbase.ClientBase.__subclasses__():
            bait_name = b.__name__.lower()
            if bait_name in entry:
                bait_options = entry[bait_name]
                dispatcher = BaitDispatcher(b, bait_options)
                dispatcher.start()
                self.dispatcher_greenlets.append(dispatcher)
                logger.info('Adding {0} bait'.format(bait_name))
                logger.debug('Bait added with options: {0}'.format(
                    bait_options))
    gevent.joinall(self.dispatcher_greenlets)