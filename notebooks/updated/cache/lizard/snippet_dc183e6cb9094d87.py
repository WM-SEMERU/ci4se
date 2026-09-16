def forward_list(self):
    version = self.version()
    if int(version[1]) <= 1 and int(version[2]) <= 0 and int(version[3]) < 31:
        raise EnvironmentError('Low adb version.')
    lines = self.run_cmd('forward', '--list').strip().splitlines()
    return [line.strip().split() for line in lines]