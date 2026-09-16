def system(command, answer=''):
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout
        =subprocess.PIPE, stderr=subprocess.PIPE, close_fds=MUST_CLOSE_FDS)
    i, o, e = p.stdin, p.stdout, p.stderr
    if answer:
        i.write(answer)
    i.close()
    result = o.read() + e.read()
    o.close()
    e.close()
    return result.decode('utf8')