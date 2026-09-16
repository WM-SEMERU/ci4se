def get_version():
    proc = subprocess.Popen(('git', 'describe', '--tag', '--always'),
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, _ = proc.communicate()
    result = output.decode('utf-8').strip()
    if proc.returncode != 0:
        sys.stderr.write('>>> Git Describe Error:\n    ' + result)
        return '1+unknown'
    split = result.split('-', 1)
    version = '+'.join(split).replace('-', '.')
    if len(split) > 1:
        sys.stderr.write('>>> Please verify the commit tag:\n    ' +
            version + '\n')
    return version