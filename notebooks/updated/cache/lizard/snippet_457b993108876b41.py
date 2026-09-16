def system_with_timeout(i):
    import subprocess
    import time
    cmd = i['cmd']
    rc = 0
    to = i.get('timeout', '')
    p = subprocess.Popen(cmd, shell=True)
    if to != '':
        xto = float(to)
        t0 = time.time()
        t = 0
        tx = float(i['timeout'])
        while p.poll() == None and t < xto:
            time.sleep(0.1)
            t = time.time() - t0
        if t >= xto and p.poll() == None:
            system_with_timeout_kill(p)
            return {'return': 8, 'error':
                'process timed out and had been terminated'}
    else:
        p.wait()
    rc = p.returncode
    return {'return': 0, 'return_code': rc}