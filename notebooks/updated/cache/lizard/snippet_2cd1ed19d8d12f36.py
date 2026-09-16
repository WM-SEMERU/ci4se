def save_file(self, title='Save As', initialDir='~', fileTypes=
    '*|All Files', rememberAs=None, **kwargs):
    if rememberAs is not None:
        return self._run_kdialog(title, ['--getsavefilename', initialDir,
            fileTypes, ':' + rememberAs], kwargs)
    else:
        return self._run_kdialog(title, ['--getsavefilename', initialDir,
            fileTypes], kwargs)