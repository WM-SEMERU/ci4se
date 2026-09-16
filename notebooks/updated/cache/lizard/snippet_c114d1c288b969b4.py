def segmentlistdict_fromsearchsummary_out(xmldoc, program=None):
    stbl = lsctables.SearchSummaryTable.get_table(xmldoc)
    ptbl = lsctables.ProcessTable.get_table(xmldoc)
    return stbl.get_out_segmentlistdict(program and ptbl.get_ids_by_program
        (program))