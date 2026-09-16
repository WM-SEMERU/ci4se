def _CreateSudoersGroup(self):
    if not self._GetGroup(self.google_sudoers_group):
        try:
            command = self.groupadd_cmd.format(group=self.google_sudoers_group)
            subprocess.check_call(command.split(' '))
        except subprocess.CalledProcessError as e:
            self.logger.warning('Could not create the sudoers group. %s.',
                str(e))
    if not os.path.exists(self.google_sudoers_file):
        try:
            with open(self.google_sudoers_file, 'w') as group:
                message = '%{0} ALL=(ALL:ALL) NOPASSWD:ALL'.format(self.
                    google_sudoers_group)
                group.write(message)
        except IOError as e:
            self.logger.error('Could not write sudoers file. %s. %s', self.
                google_sudoers_file, str(e))
            return
    file_utils.SetPermissions(self.google_sudoers_file, mode=288, uid=0, gid=0)