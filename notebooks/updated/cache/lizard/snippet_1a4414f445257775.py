def remove_not_requested_analyses_view(portal):
    logger.info("Removing 'Analyses not requested' view ...")
    ar_ptype = portal.portal_types.AnalysisRequest
    ar_ptype._actions = filter(lambda act: act.id !=
        'analyses_not_requested', ar_ptype.listActions())