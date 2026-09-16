def after_unassign(reference_analysis):
    analysis_events.after_unassign(reference_analysis)
    ref_sample = reference_analysis.aq_parent
    ref_sample.manage_delObjects([reference_analysis.getId()])