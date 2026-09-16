def assigned_state(instance):
    analyses = instance.getAnalyses()
    if not analyses:
        return 'unassigned'
    for analysis in analyses:
        analysis_object = api.get_object(analysis)
        if not analysis_object.getWorksheet():
            return 'unassigned'
    return 'assigned'