def decode(self, ids, strip_extraneous=False):
    del strip_extraneous
    return ' '.join([str(i) for i in ids])