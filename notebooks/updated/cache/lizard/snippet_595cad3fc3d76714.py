def addDuplicateAnalyses(self, src_slot, dest_slot=None):
    if api.get_workflow_status_of(self) != 'open':
        return []
    slot_from = to_int(src_slot, 0)
    if slot_from < 1:
        return []
    slot_to = to_int(dest_slot, 0)
    if slot_to < 0:
        return []
    if not slot_to:
        slot_to = self.get_suitable_slot_for_duplicate(slot_from)
        return self.addDuplicateAnalyses(src_slot, slot_to)
    processed = map(lambda an: api.get_uid(an.getAnalysis()), self.
        get_analyses_at(slot_to))
    src_analyses = list()
    for analysis in self.get_analyses_at(slot_from):
        if api.get_uid(analysis) in processed:
            if api.get_workflow_status_of(analysis) != 'retracted':
                continue
        src_analyses.append(analysis)
    ref_gid = None
    duplicates = list()
    for analysis in src_analyses:
        duplicate = self.add_duplicate_analysis(analysis, slot_to, ref_gid)
        if not duplicate:
            continue
        ref_gid = ref_gid or duplicate.getReferenceAnalysesGroupID()
        duplicates.append(duplicate)
    return duplicates