def run(self):
    for worker_pool in self.workers.values():
        worker_pool.start()
    if isinstance(self.listen, list):
        for i in self.listen:
            self.socket.connect(i)
    else:
        self.socket.connect(self.listen)
    try:
        while True:
            msg = self.socket.recv_string()
            lst = msg.split()
            if len(lst) == 2:
                topic, pks = lst[0], [lst[1]]
            elif len(lst) > 2:
                topic, pks = lst[0], lst[1:]
            else:
                self.logger.error('msg corrupt -> %s' % msg)
                continue
            self.logger.debug('replicator: {0} -> {1}'.format(topic, pks))
            for pk in pks:
                self.worker_queues[topic][str(hash(pk))].put(pk)
    except Exception as e:
        self.logger.exception(e)
    finally:
        for worker_pool in self.workers.values():
            worker_pool.terminate()