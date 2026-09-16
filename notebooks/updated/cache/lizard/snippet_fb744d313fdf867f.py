def subst_src_suffixes(self, env):
    memo_key = id(env)
    try:
        memo_dict = self._memo['subst_src_suffixes']
    except KeyError:
        memo_dict = {}
        self._memo['subst_src_suffixes'] = memo_dict
    else:
        try:
            return memo_dict[memo_key]
        except KeyError:
            pass
    suffixes = [env.subst(x) for x in self.src_suffix]
    memo_dict[memo_key] = suffixes
    return suffixes