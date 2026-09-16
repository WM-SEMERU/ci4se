def p0f_getlocalsigs():
    pid = os.fork()
    port = random.randint(30000, 40000)
    if pid > 0:
        result = {}

        def addresult(res):
            if res[0] not in result:
                result[res[0]] = [res[1]]
            elif res[1] not in result[res[0]]:
                result[res[0]].append(res[1])
        iface = conf.route.route('127.0.0.1')[0]
        count = 14
        pl = sniff(iface=iface, filter='tcp and port ' + str(port), count=
            count, timeout=3)
        map(addresult, map(packet2p0f, pl))
        os.waitpid(pid, 0)
    elif pid < 0:
        log_runtime.error('fork error')
    else:
        time.sleep(1)
        s1 = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
        try:
            s1.connect(('127.0.0.1', port))
        except socket.error:
            pass
        s1.bind(('127.0.0.1', port))
        s1.connect(('127.0.0.1', port))
        s1.close()
        os._exit(0)
    return result