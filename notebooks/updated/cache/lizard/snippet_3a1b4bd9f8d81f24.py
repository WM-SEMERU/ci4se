def streamnet(np, filleddem, flowdir, acc, streamRaster, modifiedOutlet,
    streamOrder, chNetwork, chCoord, streamNet, subbasin, workingdir=None,
    mpiexedir=None, exedir=None, log_file=None, runtime_file=None, hostfile
    =None):
    fname = TauDEM.func_name('streamnet')
    return TauDEM.run(FileClass.get_executable_fullpath(fname, exedir), {
        '-fel': filleddem, '-p': flowdir, '-ad8': acc, '-src': streamRaster,
        '-o': modifiedOutlet}, workingdir, None, {'-ord': streamOrder,
        '-tree': chNetwork, '-coord': chCoord, '-net': streamNet, '-w':
        subbasin}, {'mpipath': mpiexedir, 'hostfile': hostfile, 'n': np}, {
        'logfile': log_file, 'runtimefile': runtime_file})