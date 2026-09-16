def _exit_handler(self):
    if os.path.isfile(self.cleanup_file):
        with open(self.cleanup_file, 'a') as myfile:
            myfile.write('rm ' + self.cleanup_file + '\n')
        os.chmod(self.cleanup_file, 493)
    if not self._has_exit_status:
        print('Pipeline status: {}'.format(self.status))
        self.fail_pipeline(Exception('Pipeline failure. See details above.'))
    if self.tee:
        self.tee.kill()