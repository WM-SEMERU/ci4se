def optionally_with_plugs(phase, **subplugs):
    if isinstance(phase, PhaseGroup):
        return phase.with_plugs(**subplugs)
    if isinstance(phase, collections.Iterable):
        return [optionally_with_plugs(p, **subplugs) for p in phase]
    if not isinstance(phase, phase_descriptor.PhaseDescriptor):
        phase = phase_descriptor.PhaseDescriptor.wrap_or_copy(phase)
    return phase.with_known_plugs(**subplugs)