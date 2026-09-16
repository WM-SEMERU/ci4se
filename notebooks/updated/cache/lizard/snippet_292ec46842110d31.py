def workspaces_provider(context):
    catalog = api.portal.get_tool(name='portal_catalog')
    workspaces = catalog(portal_type='ploneintranet.workspace.workspacefolder')
    current = api.content.get_uuid(context)
    terms = []
    for ws in workspaces:
        if current != ws['UID']:
            terms.append(SimpleVocabulary.createTerm(ws['UID'], ws['UID'],
                ws['Title']))
    return SimpleVocabulary(terms)