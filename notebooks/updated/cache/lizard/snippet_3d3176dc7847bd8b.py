def getLinkedRequests(self):
    rc = api.get_tool('reference_catalog')
    refs = rc.getBackReferences(self, 'AnalysisRequestAttachment')
    ars = map(lambda ref: api.get_object_by_uid(ref.sourceUID, None), refs)
    ars = filter(None, ars)
    return sorted(ars, key=api.get_path, reverse=True)