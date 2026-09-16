def _get_cores_and_type(numcores, paralleltype, scheduler):
    if scheduler is not None:
        paralleltype = 'ipython'
    if paralleltype is None:
        paralleltype = 'local'
    if not numcores or int(numcores) < 1:
        numcores = 1
    return paralleltype, int(numcores)