def get_lsf_status():
    status_count = {'RUN': 0, 'PEND': 0, 'SUSP': 0, 'USUSP': 0, 'NJOB': 0,
        'UNKNWN': 0}
    try:
        subproc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        subproc.stderr.close()
        output = subproc.stdout.readlines()
    except OSError:
        return status_count
    for line in output[1:]:
        line = line.strip().split()
        if len(line) < 5:
            continue
        status_count['NJOB'] += 1
        for k in status_count:
            if line[2] == k:
                status_count[k] += 1
    return status_count