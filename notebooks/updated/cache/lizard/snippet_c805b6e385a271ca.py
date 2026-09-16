def _complete_transaction(cleanup_only, recursive, max_attempts, run_count,
    cmd_ret_list):
    cmd = ['yum-complete-transaction']
    if cleanup_only:
        cmd.append('--cleanup-only')
    cmd_ret_list.append(__salt__['cmd.run_all'](cmd, output_loglevel=
        'trace', python_shell=False))
    if (cmd_ret_list[-1]['retcode'] == salt.defaults.exitcodes.EX_OK and
        recursive and 'No unfinished transactions left.' not in
        cmd_ret_list[-1]['stdout']):
        if run_count >= max_attempts:
            cmd_ret_list[-1]['retcode'] = salt.defaults.exitcodes.EX_GENERIC
            log.error('Attempt %s/%s exceeded `max_attempts` for command: `%s`'
                , run_count, max_attempts, ' '.join(cmd))
            raise CommandExecutionError(
                'The `max_attempts` limit was reached and unfinished transactions remain. You may wish to increase `max_attempts` or re-execute this module.'
                , info={'results': cmd_ret_list})
        else:
            return _complete_transaction(cleanup_only, recursive,
                max_attempts, run_count + 1, cmd_ret_list)
    return cmd_ret_list