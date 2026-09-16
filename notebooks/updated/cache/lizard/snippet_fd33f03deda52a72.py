def areadinf(np, angfile, sca, outlet=None, wg=None, edgecontaimination=
    False, workingdir=None, mpiexedir=None, exedir=None, log_file=None,
    runtime_file=None, hostfile=None):
    if edgecontaimination:
        in_params = {'-nc': None}
    else:
        in_params = None
    fname = TauDEM.func_name('areadinf')
    return TauDEM.run(FileClass.get_executable_fullpath(fname, exedir), {
        '-ang': angfile, '-o': outlet, '-wg': wg}, workingdir, in_params, {
        '-sca': sca}, {'mpipath': mpiexedir, 'hostfile': hostfile, 'n': np},
        {'logfile': log_file, 'runtimefile': runtime_file})