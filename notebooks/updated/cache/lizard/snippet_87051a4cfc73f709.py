def run_script(scriptfile):
    try:
        f = open(scriptfile, mode='r')
    except Exception:
        return
    mpstate.console.writeln('Running script %s' % scriptfile)
    sub = mp_substitute.MAVSubstitute()
    for line in f:
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue
        try:
            line = sub.substitute(line, os.environ)
        except mp_substitute.MAVSubstituteError as ex:
            print('Bad variable: %s' % str(ex))
            if mpstate.settings.script_fatal:
                sys.exit(1)
            continue
        if line.startswith('@'):
            line = line[1:]
        else:
            mpstate.console.writeln('-> %s' % line)
        process_stdin(line)
    f.close()