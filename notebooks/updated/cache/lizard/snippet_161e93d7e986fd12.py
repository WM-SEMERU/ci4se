def _get_services(self, full_objects=False):
    bsc = api.get_tool('bika_setup_catalog')
    brains = bsc(portal_type='AnalysisService')
    if full_objects:
        return map(api.get_object, brains)
    return brains