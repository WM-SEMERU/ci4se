def addclassifications(agdir, prop, version=None, statfeats=[0, 4, 5, 6, 7, 8]
    ):
    try:
        ag = activegit.ActiveGit(agdir)
        if version:
            ag.set_version(version)
        clf = ag.classifier
        score = clf.predict_proba(np.nan_to_num(prop[:, (statfeats)]))[:, (1)]
        return score
    except:
        logger.info(
            'Failure when parsing activegit repo or applying classification.\n{0}'
            .format(sys.exc_info()[0]))
        return []