def verify_selenium_server_is_running(self):
    selenium_jar = settings.SELENIUM_JAR_PATH
    if len(selenium_jar) < 5:
        self.stdout.write('You need to configure SELENIUM_JAR_PATH')
        return False, None
    _jar_dir, jar_name = os.path.split(selenium_jar)
    process = Popen(['ps -e | grep "%s"' % jar_name[:-4]], shell=True,
        stdout=PIPE)
    grep_output, _grep_error = process.communicate()
    lines = grep_output.split('\n')
    for line in lines:
        if jar_name in line:
            self.stdout.write('Selenium standalone server is already running')
            return True, None
    self.stdout.write('Starting the Selenium standalone server')
    output = OutputMonitor()
    selenium_process = Popen(['java', '-jar', selenium_jar], stdout=open(os
        .devnull, 'w'), stderr=output.stream.input)
    ready_log_line = 'Selenium Server is up and running'
    if not output.wait_for(ready_log_line, 10):
        self.stdout.write('Timeout starting the Selenium server:\n')
        self.stdout.write('\n'.join(output.lines))
        return False, None
    return True, selenium_process