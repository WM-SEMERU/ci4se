def refresh_queues(self, fatal=False):
    try:
        queues = []
        prefixes = [q for q in self.config['queues'] if q.endswith('/')]
        known_subqueues = Queue.all_known(prefixes=prefixes)
        for q in self.config['queues']:
            queues.append(Queue(q))
            if q.endswith('/'):
                for subqueue in known_subqueues:
                    if subqueue.startswith(q):
                        queues.append(Queue(subqueue))
        self.queues = queues
    except Exception as e:
        self.log.error('When refreshing subqueues: %s', e)
        if fatal:
            raise