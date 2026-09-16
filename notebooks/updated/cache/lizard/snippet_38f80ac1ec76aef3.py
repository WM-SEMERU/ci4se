def open_icmp_firewall(host):
    with open(os.devnull, 'wb') as DEVNULL:
        return subprocess.Popen('ping -4 -w 1 -n 1 %s' % host, shell=True,
            stdout=DEVNULL, stderr=DEVNULL).wait()