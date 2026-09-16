def _systemctl_wait_until_finish(self, machine, unit):
    while True:
        metadata = convert_kv_to_dict(run_cmd(['systemctl', '--no-pager',
            'show', '-M', machine, unit], return_output=True))
        if not metadata['SubState'] in ['exited', 'failed']:
            time.sleep(0.1)
        else:
            break
    run_cmd(['systemctl', '--no-pager', '-M', machine, 'stop', unit],
        ignore_status=True)
    return metadata['ExecMainStatus']