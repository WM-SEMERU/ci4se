def print_cli(msg, retries=10, step=0.01):
    while retries:
        try:
            try:
                print(msg)
            except UnicodeEncodeError:
                print(msg.encode('utf-8'))
        except IOError as exc:
            err = '{0}'.format(exc)
            if exc.errno != errno.EPIPE:
                if ('temporarily unavailable' in err or exc.errno in (errno
                    .EAGAIN,)) and retries:
                    time.sleep(step)
                    retries -= 1
                    continue
                else:
                    raise
        break