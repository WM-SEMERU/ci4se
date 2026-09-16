def setup(self, puller: bool=None, subscriptions: Dict[str, Any]={}):
    if puller:
        puller = self._zmq.socket(zmq.PULL)
        ip, port, host = self.rslv('rcv')
        puller.bind('tcp://{}:{}'.format(host or ip, port))
        self.poll(puller)
    if subscriptions:
        for publisher in subscriptions:
            self.add(publisher, subscriptions[publisher].get('slots'),
                subscriptions[publisher].get('buffer-length'))
        logger.info('Listening to %s', {k: (1 if subscriptions[k].get(
            'slots') is None else len(subscriptions[k].get('slots'))) for k in
            subscriptions})