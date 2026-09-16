def terminate(self, force=False):
    if not self.isalive():
        return True
    try:
        self.kill(signal.SIGHUP)
        time.sleep(self.delayafterterminate)
        if not self.isalive():
            return True
        self.kill(signal.SIGCONT)
        time.sleep(self.delayafterterminate)
        if not self.isalive():
            return True
        self.kill(signal.SIGINT)
        time.sleep(self.delayafterterminate)
        if not self.isalive():
            return True
        if force:
            self.kill(signal.SIGKILL)
            time.sleep(self.delayafterterminate)
            if not self.isalive():
                return True
            else:
                return False
        return False
    except OSError:
        time.sleep(self.delayafterterminate)
        if not self.isalive():
            return True
        else:
            return False