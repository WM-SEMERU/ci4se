def prefixed_name(self, unprefixed_name, max_length=0):
    if max_length == 0:
        prefixed_name = '%s-%s' % (self.uuid[:8], unprefixed_name)
    else:
        if max_length < 6:
            raise RuntimeError("Can't prefix with less than 6 chars (%s)" %
                unprefixed_name)
        if max_length < 16:
            _uuid = self.uuid[:4]
        else:
            _uuid = self.uuid[:8]
        name_max_length = max_length - len(_uuid) - 1
        if name_max_length < len(unprefixed_name):
            hashed_name = hashlib.sha1(unprefixed_name).hexdigest()
            unprefixed_name = hashed_name[:name_max_length]
        prefixed_name = '%s-%s' % (_uuid, unprefixed_name)
    return prefixed_name