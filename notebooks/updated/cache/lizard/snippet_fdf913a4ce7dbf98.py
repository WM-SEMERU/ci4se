def satisfy_one(self, assumptions=None, **params):
    verbosity = params.get('verbosity', 0)
    default_phase = params.get('default_phase', 2)
    propagation_limit = params.get('propagation_limit', -1)
    decision_limit = params.get('decision_limit', -1)
    seed = params.get('seed', 1)
    return picosat.satisfy_one(self.nvars, self.clauses, assumptions,
        verbosity, default_phase, propagation_limit, decision_limit, seed)