def ces(subsystem, mechanisms=False, purviews=False, cause_purviews=False,
    effect_purviews=False, parallel=False):
    if mechanisms is False:
        mechanisms = utils.powerset(subsystem.node_indices, nonempty=True)
    engine = ComputeCauseEffectStructure(mechanisms, subsystem, purviews,
        cause_purviews, effect_purviews)
    return CauseEffectStructure(engine.run(parallel or config.
        PARALLEL_CONCEPT_EVALUATION), subsystem=subsystem)