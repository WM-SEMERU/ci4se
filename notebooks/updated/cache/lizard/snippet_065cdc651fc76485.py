def add_transition(self, source: str, dest: str):
    self._transitions[source].append(dest)