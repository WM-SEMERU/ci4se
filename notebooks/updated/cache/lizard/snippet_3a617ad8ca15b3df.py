def netbsd_interfaces():
    if LooseVersion(os.uname()[2]) < LooseVersion('8.0'):
        return linux_interfaces()
    ifconfig_path = salt.utils.path.which('ifconfig')
    cmd = subprocess.Popen('{0} -a'.format(ifconfig_path), shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
    return _netbsd_interfaces_ifconfig(salt.utils.stringutils.to_str(cmd))