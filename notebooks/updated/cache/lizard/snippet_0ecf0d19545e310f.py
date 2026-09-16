def verify_sauce_connect_is_running(self, options):
    sc_path = settings.SELENIUM_SAUCE_CONNECT_PATH
    if len(sc_path) < 2:
        self.stdout.write('You need to configure SELENIUM_SAUCE_CONNECT_PATH')
        return False, None
    username = settings.SELENIUM_SAUCE_USERNAME
    if not username:
        self.stdout.write('You need to configure SELENIUM_SAUCE_USERNAME')
        return False, None
    key = settings.SELENIUM_SAUCE_API_KEY
    if not key:
        self.stdout.write('You need to configure SELENIUM_SAUCE_API_KEY')
        return False, None
    process = Popen(['ps -e | grep "%s"' % key], shell=True, stdout=PIPE)
    grep_output, _grep_error = process.communicate()
    grep_command = 'grep {}'.format(key)
    lines = grep_output.split('\n')
    for line in lines:
        if 'sc' in line and username in line and grep_command not in line:
            self.stdout.write('Sauce Connect is already running')
            return True, None
    self.stdout.write('Starting Sauce Connect')
    output = OutputMonitor()
    command = [sc_path, '-u', username, '-k', key]
    tunnel_id = options['tunnel_id']
    if tunnel_id:
        command.extend(['-i', tunnel_id])
    sc_process = Popen(command, stdout=output.stream.input, stderr=open(os.
        devnull, 'w'), universal_newlines=True)
    ready_log_line = 'Connection established.'
    if not output.wait_for(ready_log_line, 60):
        self.stdout.write('Timeout starting Sauce Connect:\n')
        self.stdout.write('\n'.join(output.lines))
        return False, None
    return True, sc_process