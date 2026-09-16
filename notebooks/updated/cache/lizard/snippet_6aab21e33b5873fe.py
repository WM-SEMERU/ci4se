def onPersonRemoved(self, mid=None, removed_id=None, author_id=None,
    thread_id=None, ts=None, msg=None):
    log.info('{} removed: {} in {}'.format(author_id, removed_id, thread_id))