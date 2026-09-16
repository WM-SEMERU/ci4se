def pop_all(self, event_name):
    if not self.started:
        raise IllegalStateError(
            'Dispatcher needs to be started before popping.')
    results = []
    try:
        self.lock.acquire()
        while True:
            e = self.event_dict[event_name].get(block=False)
            results.append(e)
    except (queue.Empty, KeyError):
        return results
    finally:
        self.lock.release()