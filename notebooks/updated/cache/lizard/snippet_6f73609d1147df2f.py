def remove_bika_listing_resources(portal):
    logger.info('Removing bika_listing resouces')
    REMOVE_JS = ['++resource++bika.lims.js/bika.lims.bikalisting.js',
        '++resource++bika.lims.js/bika.lims.bikalistingfilterbar.js']
    REMOVE_CSS = ['bika_listing.css']
    for js in REMOVE_JS:
        logger.info('********** Unregistering JS %s' % js)
        portal.portal_javascripts.unregisterResource(js)
    for css in REMOVE_CSS:
        logger.info('********** Unregistering CSS %s' % css)
        portal.portal_css.unregisterResource(css)