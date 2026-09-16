def create_filehandlers(self, filenames, fh_kwargs=None):
    filenames = list(OrderedDict.fromkeys(filenames))
    logger.debug('Assigning to %s: %s', self.info['name'], filenames)
    self.info.setdefault('filenames', []).extend(filenames)
    filename_set = set(filenames)
    created_fhs = {}
    for filetype, filetype_info in self.sorted_filetype_items():
        filehandlers = self.new_filehandlers_for_filetype(filetype_info,
            filename_set, fh_kwargs=fh_kwargs)
        filename_set -= set([fhd.filename for fhd in filehandlers])
        if filehandlers:
            created_fhs[filetype] = filehandlers
            self.file_handlers[filetype] = sorted(self.file_handlers.get(
                filetype, []) + filehandlers, key=lambda fhd: (fhd.
                start_time, fhd.filename))
    self.update_ds_ids_from_file_handlers()
    self.add_ds_ids_from_files()
    return created_fhs