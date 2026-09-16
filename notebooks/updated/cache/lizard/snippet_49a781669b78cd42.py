def observe_id(self):
    if self._observe_id is None:
        hasher = hashlib.sha256()
        hasher.update(self.viewset_class.__module__.encode('utf8'))
        hasher.update(self.viewset_class.__name__.encode('utf8'))
        hasher.update(self.viewset_method.encode('utf8'))
        for key in sorted(self.GET.keys()):
            hasher.update(key.encode('utf8'))
            hasher.update(self.GET[key].encode('utf8'))
        hasher.update(self.path.encode('utf8'))
        hasher.update(self.path_info.encode('utf8'))
        if self._force_auth_user is not None:
            hasher.update((str(self._force_auth_user.id) or 'anonymous').
                encode('utf8'))
        else:
            hasher.update(b'anonymous')
        self._observe_id = hasher.hexdigest()
    return self._observe_id