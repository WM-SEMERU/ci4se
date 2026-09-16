def check_statement(self, stmt, max_paths=1, max_path_length=5):
    self.get_im()
    if not isinstance(stmt, (Modification, RegulateAmount, RegulateActivity,
        Influence)):
        return PathResult(False, 'STATEMENT_TYPE_NOT_HANDLED', max_paths,
            max_path_length)
    if isinstance(stmt, Modification):
        target_polarity = -1 if isinstance(stmt, RemoveModification) else 1
    elif isinstance(stmt, RegulateActivity):
        target_polarity = 1 if stmt.is_activation else -1
    elif isinstance(stmt, RegulateAmount):
        target_polarity = -1 if isinstance(stmt, DecreaseAmount) else 1
    elif isinstance(stmt, Influence):
        target_polarity = -1 if stmt.overall_polarity() == -1 else 1
    subj, obj = stmt.agent_list()
    if subj is not None:
        subj_mps = list(pa.grounded_monomer_patterns(self.model, subj,
            ignore_activities=True))
        if not subj_mps:
            logger.debug('No monomers found corresponding to agent %s' % subj)
            return PathResult(False, 'SUBJECT_MONOMERS_NOT_FOUND',
                max_paths, max_path_length)
    else:
        subj_mps = [None]
    obs_names = self.stmt_to_obs[stmt]
    if not obs_names:
        logger.debug('No observables for stmt %s, returning False' % stmt)
        return PathResult(False, 'OBSERVABLES_NOT_FOUND', max_paths,
            max_path_length)
    for subj_mp, obs_name in itertools.product(subj_mps, obs_names):
        result = self._find_im_paths(subj_mp, obs_name, target_polarity,
            max_paths, max_path_length)
        if result.path_found:
            return result
    return PathResult(False, 'NO_PATHS_FOUND', max_paths, max_path_length)