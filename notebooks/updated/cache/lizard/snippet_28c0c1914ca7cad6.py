def setCmd(self, cmd):
    cmd = cmd.upper()
    if cmd not in VALID_COMMANDS:
        raise FrameError(
            "The cmd '%s' is not valid! It must be one of '%s' (STOMP v%s)." %
            (cmd, VALID_COMMANDS, STOMP_VERSION))
    else:
        self._cmd = cmd