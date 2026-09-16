def wait_for_run(server, project, run, apikey, timeout=None, update_period=1):
    for status in watch_run_status(server, project, run, apikey, timeout,
        update_period):
        pass
    return status