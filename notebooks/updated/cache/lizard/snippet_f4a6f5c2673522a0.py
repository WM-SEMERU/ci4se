def get_object_by_uid(self, uid):
    logger.debug('get_object_by_uid::UID={}'.format(uid))
    obj = api.get_object_by_uid(uid, None)
    if obj is None:
        logger.warn('!! No object found for UID #{} !!')
    return obj