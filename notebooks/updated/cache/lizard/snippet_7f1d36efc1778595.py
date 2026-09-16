def _reducedProtToPeps(protToPeps, proteins):
    return {k: v for k, v in viewitems(protToPeps) if k not in proteins}