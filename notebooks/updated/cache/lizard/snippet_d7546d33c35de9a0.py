def chdir(self, directory=None, browsing_history=False):
    if directory is not None:
        directory = osp.abspath(to_text_string(directory))
    if browsing_history:
        directory = self.history[self.histindex]
    elif directory in self.history:
        self.histindex = self.history.index(directory)
    else:
        if self.histindex is None:
            self.history = []
        else:
            self.history = self.history[:self.histindex + 1]
        if len(self.history) == 0 or self.history and self.history[-1
            ] != directory:
            self.history.append(directory)
        self.histindex = len(self.history) - 1
    directory = to_text_string(directory)
    try:
        PermissionError
        FileNotFoundError
    except NameError:
        PermissionError = OSError
        if os.name == 'nt':
            FileNotFoundError = WindowsError
        else:
            FileNotFoundError = IOError
    try:
        os.chdir(directory)
        self.sig_open_dir.emit(directory)
        self.refresh(new_path=directory, force_current=True)
    except PermissionError:
        QMessageBox.critical(self.parent_widget, 'Error', _(
            "You don't have the right permissions to open this directory"))
    except FileNotFoundError:
        self.history.pop(self.histindex)