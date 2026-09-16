def random_sparse(strategy, prob, obj_reaction, flux_threshold):
    essential = set()
    deleted = set()
    for entity, deleted_reactions in strategy.iter_tests():
        if obj_reaction in deleted_reactions:
            logger.info(
                'Marking entity {} as essential because the objective reaction depends on this entity...'
                .format(entity))
            essential.add(entity)
            continue
        if len(deleted_reactions) == 0:
            logger.info('No reactions were removed when entity {} was deleted'
                .format(entity))
            deleted.add(entity)
            strategy.delete(entity, deleted_reactions)
            continue
        logger.info('Deleted reactions: {}'.format(', '.join(
            deleted_reactions)))
        constr = []
        for r in deleted_reactions:
            flux_var = prob.get_flux_var(r)
            c, = prob.prob.add_linear_constraints(flux_var == 0)
            constr.append(c)
        logger.info('Trying FBA without reactions {}...'.format(', '.join(
            deleted_reactions)))
        try:
            prob.maximize(obj_reaction)
        except fluxanalysis.FluxBalanceError:
            logger.info('FBA is infeasible, marking {} as essential'.format
                (entity))
            for c in constr:
                c.delete()
            essential.add(entity)
            continue
        logger.debug('Reaction {} has flux {}'.format(obj_reaction, prob.
            get_flux(obj_reaction)))
        if prob.get_flux(obj_reaction) < flux_threshold:
            for c in constr:
                c.delete()
            essential.add(entity)
            logger.info('Entity {} was essential'.format(entity))
        else:
            deleted.add(entity)
            strategy.delete(entity, deleted_reactions)
            logger.info('Entity {} was deleted'.format(entity))
    return essential, deleted