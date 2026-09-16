def _redis_process_checkpoint(host, port):
    try:
        subprocess.check_output('pgrep redis', shell=True)
    except Exception:
        logger.warning(
            'Your redis server is offline, fake2db will try to launch it now!',
            extra=extra_information)
        subprocess.Popen('redis-server --bind %s --port %s' % (host, port),
            close_fds=True, shell=True)
        time.sleep(3)