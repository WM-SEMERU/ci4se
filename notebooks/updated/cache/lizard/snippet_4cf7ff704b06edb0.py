def start(self):
    assert not self.is_running(
        ), 'Attempted to start an energy measurement while one was already running.'
    self._measurement_process = subprocess.Popen([self._executable, '-r'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=10000,
        preexec_fn=os.setpgrp)