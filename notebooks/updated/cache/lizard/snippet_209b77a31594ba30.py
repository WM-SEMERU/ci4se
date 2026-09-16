def get_scripts():
    proc = Popen(['npm', 'run-script'], stdout=PIPE)
    should_yeild = False
    for line in proc.stdout.readlines():
        line = line.decode()
        if 'available via `npm run-script`:' in line:
            should_yeild = True
            continue
        if should_yeild and re.match('^  [^ ]+', line):
            yield line.strip().split(' ')[0]