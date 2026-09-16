def _kill_child_process(self, child_pid, proc_name=None):

    def pskill(proc_pid, sig=signal.SIGINT):
        parent_process = psutil.Process(proc_pid)
        for child_proc in parent_process.children(recursive=True):
            child_proc.send_signal(sig)
        parent_process.send_signal(sig)
    if child_pid is None:
        return
    if proc_name:
        proc_string = ' ({proc_name})'.format(proc_name=proc_name)
    sys.stdout.flush()
    still_running = self._attend_process(psutil.Process(child_pid), 0)
    sleeptime = 0.25
    time_waiting = 0
    while still_running and time_waiting < 3:
        try:
            if time_waiting > 2:
                pskill(child_pid, signal.SIGKILL)
            elif time_waiting > 1:
                pskill(child_pid, signal.SIGTERM)
            else:
                pskill(child_pid, signal.SIGINT)
        except OSError:
            still_running = False
            time_waiting = time_waiting + sleeptime
        time_waiting = time_waiting + sleeptime
        if not self._attend_process(psutil.Process(child_pid), sleeptime):
            still_running = False
    if still_running:
        print(
            "Child process {child_pid}{proc_string} never respondedI just can't take it anymore. I don't know what to do..."
            .format(child_pid=child_pid, proc_string=proc_string))
    else:
        if time_waiting > 0:
            note = 'terminated after {time} sec'.format(time=int(time_waiting))
        else:
            note = 'was already terminated'
        msg = 'Child process {child_pid}{proc_string} {note}.'.format(child_pid
            =child_pid, proc_string=proc_string, note=note)
        print(msg)