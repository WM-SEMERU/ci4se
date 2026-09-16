def enqueue(self, item, queue=None):
    if queue is None:
        queue = self.queue
    is_enqueue_item = True
    if self.invalid_key_list is not None:
        for entry in self.invalid_key_list:
            if entry in item.data['key']:
                is_enqueue_item = False
                log_message = ('{key} is filtered by "invalid_key_list".'.
                    format(key=item.data['key'], plugin=__name__))
                self.logger.debug(log_message)
                break
    if is_enqueue_item:
        try:
            queue.put(item, block=False)
            return True
        except Full:
            self.logger.error('Blackbird item Queue is Full!!!')
            return False
    else:
        return False