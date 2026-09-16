def _add_epsilon_states(self, stateset, gathered_epsilons):
    for i in list(stateset):
        if i not in gathered_epsilons:
            gathered_epsilons[i] = {}
            q = _otq()
            q.append(i)
            while q:
                s = q.popleft()
                for j in self._transitions.setdefault(s, {}).setdefault(NFA
                    .EPSILON, set()):
                    gathered_epsilons[i][j] = s if j not in gathered_epsilons[i
                        ] else self.choose(s, j)
                    q.append(j)
        stateset.update(gathered_epsilons[i].keys())