def dropanalysis(np, fel, p, ad8, ssa, outlet, minthresh, maxthresh,
    numthresh, logspace, drp, workingdir=None, mpiexedir=None, exedir=None,
    log_file=None, runtime_file=None, hostfile=None):
    parstr = '%f %f %f' % (minthresh, maxthresh, numthresh)
    if logspace == 'false':
        parstr += ' 1'
    else:
        parstr += ' 0'
    fname = TauDEM.func_name('dropanalysis')
    return TauDEM.run(FileClass.get_executable_fullpath(fname, exedir), {
        '-fel': fel, '-p': p, '-ad8': ad8, '-ssa': ssa, '-o': outlet},
        workingdir, {'-par': parstr}, {'-drp': drp}, {'mpipath': mpiexedir,
        'hostfile': hostfile, 'n': np}, {'logfile': log_file, 'runtimefile':
        runtime_file})