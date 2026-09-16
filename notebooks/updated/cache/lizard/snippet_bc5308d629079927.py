def anim(self, duration, offset=0, timestep=1, label=None, unit=None,
    time_fn=param.Dynamic.time_fn):
    frames = duration // timestep + 1
    if duration % timestep != 0:
        raise ValueError(
            'The duration value must be an exact multiple of the timestep.')
    if label is None:
        label = time_fn.label if hasattr(time_fn, 'label') else 'Time'
    unit = time_fn.unit if not unit and hasattr(time_fn, 'unit') else unit
    vmap = HoloMap(kdims=[Dimension(label, unit=unit if unit else '')])
    self.state_push()
    with time_fn as t:
        t(offset)
        for i in range(frames):
            vmap[t()] = self[:]
            t += timestep
    self.state_pop()
    return vmap