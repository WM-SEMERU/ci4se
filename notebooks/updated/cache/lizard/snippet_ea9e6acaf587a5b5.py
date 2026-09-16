def find_installed_packages(self):
    list_command = subprocess.Popen(self.list_command, shell=True, stdout=
        subprocess.PIPE)
    stdout, stderr = list_command.communicate()
    if list_command.returncode != 0:
        raise SystemDependencyError(
            'The command to list the installed system packages failed! ({command})'
            , command=self.list_command)
    installed_packages = sorted(stdout.decode().split())
    logger.debug('Found %i installed system package(s): %s', len(
        installed_packages), installed_packages)
    return installed_packages