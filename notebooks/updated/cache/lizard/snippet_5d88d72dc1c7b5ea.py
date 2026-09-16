def cause_info(self, mechanism, purview):
    return repertoire_distance(Direction.CAUSE, self.cause_repertoire(
        mechanism, purview), self.unconstrained_cause_repertoire(purview))