def _get_result_paths(self, data):
    wd = self.WorkingDir
    db_name = self.Parameters['-n'].Value
    log_name = self.Parameters['-l'].Value
    result = {}
    result['log'] = ResultPath(Path=wd + log_name, IsWritten=True)
    if self.Parameters['-p'].Value == 'F':
        extensions = ['nhr', 'nin', 'nsq', 'nsd', 'nsi']
    else:
        extensions = ['phr', 'pin', 'psq', 'psd', 'psi']
    for extension in extensions:
        for file_path in glob(wd + (db_name + '*' + extension)):
            key = file_path.split(db_name + '.')[1]
            result_path = ResultPath(Path=file_path, IsWritten=True)
            result[key] = result_path
    return result