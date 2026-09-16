def get_program(self, n, timeout=2.0, max_retries=2):
    response = self.driver.send_command('TPROG PROG' + str(int(n)), timeout
        =timeout, immediate=True, max_retries=max_retries)
    if self.driver.command_error(response) or len(response[4]) == 0:
        return []
    else:
        if '*END' in response[4]:
            response[4].remove('*END')
        return [line[1:] for line in response[4]]