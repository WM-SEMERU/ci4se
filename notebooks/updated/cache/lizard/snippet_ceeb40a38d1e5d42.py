def active(self, subject_id, entity_id):
    item = self._cache.find_one({'subject_id': subject_id, 'entity_id':
        entity_id})
    try:
        return time_util.not_on_or_after(item['timestamp'])
    except ToOld:
        return False