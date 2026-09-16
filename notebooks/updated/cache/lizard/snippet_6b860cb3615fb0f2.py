def _range_func(self, withscores, score_cast_func):
    if withscores:
        return lambda score_member: (score_member[1], score_cast_func(self.
            _encode(score_member[0])))
    else:
        return lambda score_member: score_member[1]