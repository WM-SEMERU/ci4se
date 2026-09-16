def get_tags(self, rev=None):
    rev_num = self._get_rev_num(rev)
    return set(self._read_tags_for_rev(rev_num)) if not rev_num.endswith('+'
        ) else set([])