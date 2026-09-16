def check(conn, command, exit=False, timeout=None, **kw):
    command = conn.cmd(command)
    stop_on_error = kw.pop('stop_on_error', True)
    timeout = timeout or conn.global_timeout
    if not kw.get('env'):
        kw = extend_env(conn, kw)
    conn.logger.info('Running command: %s' % ' '.join(admin_command(conn.
        sudo, command)))
    result = conn.execute(_remote_check, cmd=command, **kw)
    response = None
    try:
        response = result.receive(timeout)
    except Exception as err:
        if err.__class__.__name__ == 'TimeoutError':
            msg = (
                'No data was received after %s seconds, disconnecting...' %
                timeout)
            conn.logger.warning(msg)
            return [], [], -1
        else:
            remote_trace = traceback.format_exc()
            remote_error = RemoteError(remote_trace)
            if remote_error.exception_name == 'RuntimeError':
                conn.logger.error(remote_error.exception_line)
            else:
                for tb_line in remote_trace.split('\n'):
                    conn.logger.error(tb_line)
            if stop_on_error:
                raise RuntimeError('Failed to execute command: %s' % ' '.
                    join(command))
    if exit:
        conn.exit()
    return response