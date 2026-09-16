def execute(asynchronous: bool=False):
    r = Response()
    r.update(server=server_runner.get_server_data())
    cmd, args = parse_command_args(r)
    if r.failed:
        return flask.jsonify(r.serialize())
    try:
        commander.execute(cmd, args, r)
        if not r.thread:
            return flask.jsonify(r.serialize())
        if not asynchronous:
            r.thread.join()
        server_runner.active_execution_responses[r.thread.uid] = r
        count = 0
        while count < 5:
            count += 1
            r.thread.join(0.25)
            if not r.thread.is_alive():
                break
        if r.thread.is_alive():
            return flask.jsonify(Response().update(run_log=r.get_thread_log
                (), run_status='running', run_uid=r.thread.uid,
                step_changes=server_runner.get_running_step_changes(True),
                server=server_runner.get_server_data()).serialize())
        del server_runner.active_execution_responses[r.thread.uid]
        r.update(run_log=r.get_thread_log(), run_status='complete',
            run_multiple_updates=False, run_uid=r.thread.uid)
    except Exception as err:
        r.fail(code='KERNEL_EXECUTION_FAILURE', message=
            'Unable to execute command', cmd=cmd, args=args, error=err)
    return flask.jsonify(r.serialize())