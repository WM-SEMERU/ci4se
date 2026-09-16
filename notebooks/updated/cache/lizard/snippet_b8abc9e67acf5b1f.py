def pipe_commands(cmds, extra_env=None, show_stderr=False, show_last_stdout
    =False):
    env = extend_env(extra_env) if extra_env else None
    env_str = get_env_str(extra_env) + ' ' if extra_env else ''
    cmd_strs = [(env_str + ' '.join(cmd)) for cmd in cmds]
    logger.info('Running `{0}`'.format(' | '.join(cmd_strs)))
    with open('/dev/null', 'w') as NULL:
        processes = []
        last_i = len(cmds) - 1
        for i, (cmd_str, cmd) in enumerate(zip(cmd_strs, cmds)):
            if i == last_i:
                p_stdout = None if show_last_stdout else NULL
            else:
                p_stdout = PIPE
            p_stdin = processes[-1][1].stdout if processes else None
            p_stderr = None if show_stderr else NULL
            p = Popen(cmd, env=env, stdout=p_stdout, stdin=p_stdin, stderr=
                p_stderr)
            processes.append((cmd_str, p))
        error = False
        for cmd_str, p in processes:
            if p.stdout:
                p.stdout.close()
            if p.wait() != 0:
                error = True
        if error:
            raise CalledProcessError(cmd=cmd_str, returncode=p.returncode)