def _constraints_are_whitelisted(self, constraint_tuple):
    if self._acceptable_interpreter_constraints == []:
        return True
    return all(version.parse(constraint) in self.
        _acceptable_interpreter_constraints for constraint in constraint_tuple)