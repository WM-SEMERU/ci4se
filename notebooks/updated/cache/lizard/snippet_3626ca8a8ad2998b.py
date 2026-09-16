def apply(self, state_func=None, stash_func=None, stash='active', to_stash=None
    ):
    to_stash = to_stash or stash

    def _stash_splitter(states):
        keep, split = [], []
        if state_func is not None:
            for s in states:
                ns = state_func(s)
                if isinstance(ns, SimState):
                    split.append(ns)
                elif isinstance(ns, (list, tuple, set)):
                    split.extend(ns)
                else:
                    split.append(s)
        if stash_func is not None:
            split = stash_func(states)
        if to_stash is not stash:
            keep = states
        return keep, split
    return self.split(_stash_splitter, from_stash=stash, to_stash=to_stash)