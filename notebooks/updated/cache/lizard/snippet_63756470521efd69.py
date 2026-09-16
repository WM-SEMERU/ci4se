def dinfflowdir(np, filleddem, flowangle, slope, workingdir=None, mpiexedir
    =None, exedir=None, log_file=None, runtime_file=None, hostfile=None):
    fname = TauDEM.func_name('dinfflowdir')
    return TauDEM.run(FileClass.get_executable_fullpath(fname, exedir), {
        '-fel': filleddem}, workingdir, None, {'-ang': flowangle, '-slp':
        slope}, {'mpipath': mpiexedir, 'hostfile': hostfile, 'n': np}, {
        'logfile': log_file, 'runtimefile': runtime_file})