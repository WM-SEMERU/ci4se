def get_storage_info(self, human=False):
    res = self._req_get_storage_info()
    if human:
        res['total'] = humanize.naturalsize(res['total'], binary=True)
        res['used'] = humanize.naturalsize(res['used'], binary=True)
    return res