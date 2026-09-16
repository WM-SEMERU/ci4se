def _ssh_master_cmd(addr, user, command, local_key=None):
    ssh_call = ['ssh', '-qNfL%d:127.0.0.1:12042' % find_port(addr, user),
        '-o', 'ControlPath=~/.ssh/unixpipe_%%r@%%h_%d' % find_port(addr,
        user), '-O', command, '%s@%s' % (user, addr)]
    if local_key:
        ssh_call.insert(1, local_key)
        ssh_call.insert(1, '-i')
    return subprocess.call(ssh_call)