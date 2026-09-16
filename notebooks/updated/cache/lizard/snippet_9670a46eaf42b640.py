def kill(self, sig):
    if sys.platform == 'win32':
        if sig in [signal.SIGINT, signal.CTRL_C_EVENT]:
            sig = signal.CTRL_C_EVENT
        elif sig in [signal.SIGBREAK, signal.CTRL_BREAK_EVENT]:
            sig = signal.CTRL_BREAK_EVENT
        else:
            sig = signal.SIGTERM
    os.kill(self.proc.pid, sig)