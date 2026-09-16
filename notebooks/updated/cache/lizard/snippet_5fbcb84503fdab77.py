def kernel_version():
    kver = check_output(['uname', '-r']).decode('UTF-8').strip()
    kver = kver.split('.')
    return int(kver[0]), int(kver[1])