def commit_config(self, message=''):
    if message:
        raise NotImplementedError(
            'Commit message not implemented for this platform')
    self._gen_rollback_cfg()
    if self.config_replace:
        filename = self.candidate_cfg
        cfg_file = self._gen_full_path(filename)
        if not self._check_file_exists(cfg_file):
            raise ReplaceConfigException('Candidate config file does not exist'
                )
        if self.auto_rollback_on_error:
            cmd = 'configure replace {} force revert trigger error'.format(
                cfg_file)
        else:
            cmd = 'configure replace {} force'.format(cfg_file)
        output = self._commit_handler(cmd)
        if ('original configuration has been successfully restored' in
            output or 'error' in output.lower() or 
            'not a valid config file' in output.lower() or 'failed' in
            output.lower()):
            msg = 'Candidate config could not be applied\n{}'.format(output)
            raise ReplaceConfigException(msg)
        elif '%Please turn config archive on' in output:
            msg = (
                "napalm-ios replace() requires Cisco 'archive' feature to be enabled."
                )
            raise ReplaceConfigException(msg)
    else:
        filename = self.merge_cfg
        cfg_file = self._gen_full_path(filename)
        if not self._check_file_exists(cfg_file):
            raise MergeConfigException(
                'Merge source config file does not exist')
        cmd = 'copy {} running-config'.format(cfg_file)
        output = self._commit_handler(cmd)
        if 'Invalid input detected' in output:
            self.rollback()
            err_header = (
                'Configuration merge failed; automatic rollback attempted')
            merge_error = '{0}:\n{1}'.format(err_header, output)
            raise MergeConfigException(merge_error)
    self.prompt_quiet_configured = None
    output += self.device.save_config()