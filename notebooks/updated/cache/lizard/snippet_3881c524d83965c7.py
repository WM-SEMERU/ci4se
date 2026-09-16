def delete_all(self, filter, timeout=-1, force=False):
    return self._helper.delete_all(filter=filter, force=force, timeout=timeout)