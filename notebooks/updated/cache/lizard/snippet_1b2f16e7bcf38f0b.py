def modify_pattern(self, pattern, group):
    pattern = group_regex.sub('?P<{}_\\1>'.format(self.name), pattern)
    return '(?P<{}>{})'.format(group, pattern)