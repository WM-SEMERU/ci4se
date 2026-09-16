def get_copy_from(self):
    copy_from = self.request.form.get('copy_from', '').split(',')
    copy_from_uids = filter(lambda x: x, copy_from)
    out = dict().fromkeys(range(len(copy_from_uids)))
    for n, uid in enumerate(copy_from_uids):
        ar = self.get_object_by_uid(uid)
        if ar is None:
            continue
        out[n] = ar
    logger.info('get_copy_from: uids={}'.format(copy_from_uids))
    return out