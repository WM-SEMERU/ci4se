def _start_dev_proc(self, device_os, device_config):
    log.info('Starting the child process for %s', device_os)
    dos = NapalmLogsDeviceProc(device_os, self.opts, device_config)
    os_proc = Process(target=dos.start)
    os_proc.start()
    os_proc.description = '%s device process' % device_os
    log.debug('Started process %s for %s, having PID %s', os_proc._name,
        device_os, os_proc.pid)
    return os_proc