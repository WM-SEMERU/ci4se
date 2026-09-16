def type_check(self, filename):
    self.log.debug('type_check: in')
    self.editor.clean_errors()
    self.send_request({'typehint': 'TypecheckFilesReq', 'files': [self.
        editor.path()]})