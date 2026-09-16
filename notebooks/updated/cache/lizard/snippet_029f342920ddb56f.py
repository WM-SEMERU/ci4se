def focusd(task):
    if registration.get_registered(event_hooks=True, root_access=True):
        start_cmd_srv = os.getuid() == 0
    else:
        start_cmd_srv = False
    _run = lambda : Focusd(task).run(start_cmd_srv)
    daemonize(get_daemon_pidfile(task), task.task_dir, _run)