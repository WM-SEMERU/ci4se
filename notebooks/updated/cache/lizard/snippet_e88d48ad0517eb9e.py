def execute(filelocation, args, outdir, filters=None, executable=
    'msConvert.exe'):
    procArgs = [executable, filelocation]
    procArgs.extend(aux.toList(args))
    if filters is not None:
        for arg in aux.toList(filters):
            procArgs.extend(['--filter', arg])
    procArgs.extend(['-o', outdir])
    proc = subprocess.Popen(procArgs, stderr=subprocess.PIPE)
    while True:
        out = proc.stderr.read(1)
        if out == '' and proc.poll() != None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()