def is_submitted_or_submittable(analysis):
    if ISubmitted.providedBy(analysis):
        return True
    if wf.isTransitionAllowed(analysis, 'submit'):
        return True
    return False