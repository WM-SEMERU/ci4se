def sort_by_size(self, group_limit=None, discard_others=False, others_label
    ='others'):
    self.groups = OrderedDict(sorted(six.iteritems(self.groups), key=lambda
        x: len(x[1]), reverse=True))
    if group_limit is not None:
        if not discard_others:
            group_keys = self.groups.keys()[group_limit - 1:]
            self.groups.setdefault(others_label, list())
        else:
            group_keys = self.groups.keys()[group_limit:]
        for g in group_keys:
            if not discard_others:
                self.groups[others_label].extend(self.groups[g])
            del self.groups[g]
        if others_label in self.groups and len(self.groups[others_label]) == 0:
            del self.groups[others_label]
    if discard_others and others_label in self.groups:
        del self.groups[others_label]