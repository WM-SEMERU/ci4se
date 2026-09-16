def copy_script(self, filename, id_=-1):
    if 'jss' in self.connection.keys() and self.connection['jss'].jss_migrated:
        self._copy_script_migrated(filename, id_, SCRIPT_FILE_TYPE)
    else:
        basename = os.path.basename(filename)
        self._copy(filename, os.path.join(self.connection['mount_point'],
            'Scripts', basename))