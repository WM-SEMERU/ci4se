def _sia(cache_key, subsystem):
    log.info('Calculating big-phi data for %s...', subsystem)
    if not subsystem:
        log.info('Subsystem %s is empty; returning null SIA immediately.',
            subsystem)
        return _null_sia(subsystem)
    if not connectivity.is_strong(subsystem.cm, subsystem.node_indices):
        log.info(
            '%s is not strongly connected; returning null SIA immediately.',
            subsystem)
        return _null_sia(subsystem)
    if len(subsystem.cut_indices) == 1:
        if not subsystem.cm[subsystem.node_indices][subsystem.node_indices]:
            log.info(
                'Single micro nodes %s without selfloops cannot have phi; returning null SIA immediately.'
                , subsystem)
            return _null_sia(subsystem)
        elif not config.SINGLE_MICRO_NODES_WITH_SELFLOOPS_HAVE_PHI:
            log.info(
                'Single micro nodes %s with selfloops cannot have phi; returning null SIA immediately.'
                , subsystem)
            return _null_sia(subsystem)
    log.debug('Finding unpartitioned CauseEffectStructure...')
    unpartitioned_ces = _ces(subsystem)
    if not unpartitioned_ces:
        log.info(
            'Empty unpartitioned CauseEffectStructure; returning null SIA immediately.'
            )
        return _null_sia(subsystem)
    log.debug('Found unpartitioned CauseEffectStructure.')
    if len(subsystem.cut_indices) == 1:
        cuts = [Cut(subsystem.cut_indices, subsystem.cut_indices, subsystem
            .cut_node_labels)]
    else:
        cuts = sia_bipartitions(subsystem.cut_indices, subsystem.
            cut_node_labels)
    engine = ComputeSystemIrreducibility(cuts, subsystem, unpartitioned_ces)
    result = engine.run(config.PARALLEL_CUT_EVALUATION)
    if config.CLEAR_SUBSYSTEM_CACHES_AFTER_COMPUTING_SIA:
        log.debug('Clearing subsystem caches.')
        subsystem.clear_caches()
    log.info('Finished calculating big-phi data for %s.', subsystem)
    return result