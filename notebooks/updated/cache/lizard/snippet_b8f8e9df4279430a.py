def _get_oplog_timestamp(self, newest_entry):
    sort_order = pymongo.DESCENDING if newest_entry else pymongo.ASCENDING
    curr = self.oplog.find({'op': {'$ne': 'n'}}).sort('$natural', sort_order
        ).limit(-1)
    try:
        ts = next(curr)['ts']
    except StopIteration:
        LOG.debug('OplogThread: oplog is empty.')
        return None
    LOG.debug('OplogThread: %s oplog entry has timestamp %s.' % ('Newest' if
        newest_entry else 'Oldest', ts))
    return ts