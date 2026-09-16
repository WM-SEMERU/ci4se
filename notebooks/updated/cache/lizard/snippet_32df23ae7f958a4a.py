def __set_workdir(self):
    fname = self.get_current_filename()
    if fname is not None:
        directory = osp.dirname(osp.abspath(fname))
        self.open_dir.emit(directory)