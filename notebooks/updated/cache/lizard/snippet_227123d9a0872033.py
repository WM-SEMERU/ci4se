def complete(self, sp_args, line, rl_prefix, rl_begidx, rl_endidx):
    if len(sp_args) == 0 or not line.endswith(sp_args[-1]):
        return self.accepted_flags
    else:
        matches = []
        for arg in self.accepted_flags:
            if arg.startswith(sp_args[-1]):
                matches.append(arg)
        if len(matches) == 1:
            sub = len(sp_args[-1]) - len(rl_prefix)
            return [matches[0][sub:]]
        else:
            return matches