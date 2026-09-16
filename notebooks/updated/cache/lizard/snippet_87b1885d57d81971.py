def sscan(self, key, cursor=0, match=None, count=None):
    tokens = [key, cursor]
    match is not None and tokens.extend([b'MATCH', match])
    count is not None and tokens.extend([b'COUNT', count])
    fut = self.execute(b'SSCAN', *tokens)
    return wait_convert(fut, lambda obj: (int(obj[0]), obj[1]))