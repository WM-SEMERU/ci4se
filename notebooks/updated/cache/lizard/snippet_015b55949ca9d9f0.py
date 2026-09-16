def check_index(self, key, *, index):
    self.append({'Verb': 'check-index', 'Key': key, 'Index': extract_attr(
        index, keys=['ModifyIndex', 'Index'])})
    return self