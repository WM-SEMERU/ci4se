def inspect(self, **kwargs):
    try:
        scf_cycle = abiinspect.GroundStateScfCycle.from_file(self.
            output_file.path)
    except IOError:
        return None
    if scf_cycle is not None:
        if 'title' not in kwargs:
            kwargs['title'] = str(self)
        return scf_cycle.plot(**kwargs)
    return None