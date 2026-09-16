def get_type_id(context, **kw):
    portal_type = kw.get('portal_type', None)
    if portal_type:
        return portal_type
    if IAnalysisRequestPartition.providedBy(context):
        return 'AnalysisRequestPartition'
    elif IAnalysisRequestRetest.providedBy(context):
        return 'AnalysisRequestRetest'
    elif IAnalysisRequestSecondary.providedBy(context):
        return 'AnalysisRequestSecondary'
    return api.get_portal_type(context)