def changes_str(self):
    changes = ''
    for item in self._get_recursive_difference(type='intersect'):
        if item.diffs:
            changes = ''.join([changes, '\tidentified by {0} {1}:\n\t{2}\n'
                .format(self._key, item.past_dict[self._key], item.
                changes_str.replace('\n', '\n\t'))])
    for item in self._get_recursive_difference(type='removed'):
        if item.past_dict:
            changes = ''.join([changes,
                '\tidentified by {0} {1}:\n\twill be removed\n'.format(self
                ._key, item.past_dict[self._key])])
    for item in self._get_recursive_difference(type='added'):
        if item.current_dict:
            changes = ''.join([changes,
                '\tidentified by {0} {1}:\n\twill be added\n'.format(self.
                _key, item.current_dict[self._key])])
    return changes