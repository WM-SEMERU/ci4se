def find_step_impl(self, step):
    result = None
    for si in self.steps[step.step_type]:
        matches = si.match(step.match)
        if matches:
            if result:
                raise AmbiguousStepImpl(step, result[0], si)
            args = [self._apply_transforms(arg, si) for arg in matches.groups()
                ]
            result = si, args
    if not result:
        raise UndefinedStepImpl(step)
    return result