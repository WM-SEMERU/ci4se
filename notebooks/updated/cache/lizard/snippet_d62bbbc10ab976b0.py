def get_rank(self, member, reverse=False, pipe=None):
    pipe = self.redis if pipe is None else pipe
    method = getattr(pipe, 'zrevrank' if reverse else 'zrank')
    rank = method(self.key, self._pickle(member))
    return rank