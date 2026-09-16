def which(software, strip_newline=True):
    if software is None:
        software = 'singularity'
    cmd = ['which', software]
    try:
        result = run_command(cmd)
        if strip_newline is True:
            result['message'] = result['message'].strip('\n')
        return result
    except:
        return None