def removed(self):

    def _removed(diffs, prefix):
        keys = []
        for key in diffs.keys():
            if isinstance(diffs[key], dict) and 'old' not in diffs[key]:
                keys.extend(_removed(diffs[key], prefix='{0}{1}.'.format(
                    prefix, key)))
            elif diffs[key]['new'] == self.NONE_VALUE:
                keys.append('{0}{1}'.format(prefix, key))
            elif isinstance(diffs[key]['new'], dict):
                keys.extend(_removed(diffs[key]['new'], prefix='{0}{1}.'.
                    format(prefix, key)))
        return keys
    return sorted(_removed(self._diffs, prefix=''))