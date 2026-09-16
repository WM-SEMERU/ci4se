def rename_bika_setup():
    logger.info('Renaming Bika Setup...')
    bika_setup = api.get_bika_setup()
    bika_setup.setTitle('Setup')
    bika_setup.reindexObject()
    setup = api.get_portal().portal_setup
    setup.runImportStepFromProfile('profile-bika.lims:default', 'controlpanel')