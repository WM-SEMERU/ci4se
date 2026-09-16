def _convert_file_records(self, paths):
    ret = []
    for path in paths:
        if os.path.basename(path) == self.fs.dir_keep_file:
            continue
        type_ = self.guess_type(path, allow_directory=True)
        if type_ == 'notebook':
            ret.append(self._notebook_model_from_path(path, False))
        elif type_ == 'file':
            ret.append(self._file_model_from_path(path, False, None))
        elif type_ == 'directory':
            ret.append(self._directory_model_from_path(path, False))
        else:
            self.do_error("Unknown file type %s for file '%s'" % (type_,
                path), 500)
    return ret