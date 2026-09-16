def install_signal_trap(signums=(signal.SIGTERM, signal.SIGTSTP), retval=1):
    signums = set(signums) - set(origactions)

    def temporary_file_cleanup_on_signal(signum, frame):
        with temporary_files_lock:
            temporary_files.clear()
        if callable(origactions[signum]):
            return origactions[signum](signum, frame)
        sys.exit(retval)
    for signum in signums:
        origactions[signum] = signal.getsignal(signum)
        if origactions[signum] != signal.SIG_IGN:
            signal.signal(signum, temporary_file_cleanup_on_signal)