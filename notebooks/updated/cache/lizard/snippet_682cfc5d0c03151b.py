def _add_nested(self, rec, name, value):
    typedef, target_term = value.split('!')[0].rstrip().split(' ')
    getattr(rec, name)[typedef].append(target_term)