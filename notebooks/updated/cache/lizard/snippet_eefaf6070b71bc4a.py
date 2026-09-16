def to_1000(portal_setup):
    logger.info('Run all import steps from SENAITE LIMS ...')
    context = portal_setup._getImportContext(PROFILE_ID)
    portal = context.getSite()
    setup_html_filter(portal)
    portal_setup.runAllImportStepsFromProfile(PROFILE_ID)
    logger.info('Run all import steps from SENAITE LIMS [DONE]')