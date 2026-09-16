def isalive(self):
    if self.terminated:
        return False
    if self.flag_eof:
        waitpid_options = 0
    else:
        waitpid_options = os.WNOHANG
    try:
        pid, status = os.waitpid(self.pid, waitpid_options)
    except OSError as e:
        if e.errno == errno.ECHILD:
            raise PtyProcessError('isalive() encountered condition ' +
                'where "terminated" is 0, but there was no child ' +
                'process. Did someone else call waitpid() ' + 'on our process?'
                )
        else:
            raise
    if pid == 0:
        try:
            pid, status = os.waitpid(self.pid, waitpid_options)
        except OSError as e:
            if e.errno == errno.ECHILD:
                raise PtyProcessError('isalive() encountered condition ' +
                    'that should never happen. There was no child ' +
                    'process. Did someone else call waitpid() ' +
                    'on our process?')
            else:
                raise
        if pid == 0:
            return True
    if pid == 0:
        return True
    if os.WIFEXITED(status):
        self.status = status
        self.exitstatus = os.WEXITSTATUS(status)
        self.signalstatus = None
        self.terminated = True
    elif os.WIFSIGNALED(status):
        self.status = status
        self.exitstatus = None
        self.signalstatus = os.WTERMSIG(status)
        self.terminated = True
    elif os.WIFSTOPPED(status):
        raise PtyProcessError('isalive() encountered condition ' +
            'where child process is stopped. This is not ' +
            'supported. Is some other process attempting ' +
            'job control with our child pid?')
    return False