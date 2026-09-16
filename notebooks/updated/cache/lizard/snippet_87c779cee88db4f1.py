def stop_process(process):
    process.terminate()
    process.join(3)
    if process.is_alive() and os.name != 'nt':
        try:
            os.kill(process.pid, signal.SIGKILL)
            process.join()
        except OSError:
            return
    if process.is_alive():
        raise RuntimeError('Unable to terminate PID %d' % os.getpid())