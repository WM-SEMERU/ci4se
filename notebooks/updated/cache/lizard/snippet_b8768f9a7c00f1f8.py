def run_with_reloader(main_func, extra_files=None, interval=1):
    import signal
    signal.signal(signal.SIGTERM, lambda *args: sys.exit(0))
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        thread.start_new_thread(main_func, ())
        try:
            reloader_loop(extra_files, interval)
        except KeyboardInterrupt:
            return
    try:
        sys.exit(restart_with_reloader())
    except KeyboardInterrupt:
        pass