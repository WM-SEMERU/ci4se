def build_groups(self):
    if len(self.groups):
        groups = []
        for group in self.groups:
            groups.append(group.get_name())
        return 'GROUP BY {0} '.format(', '.join(groups))
    return ''