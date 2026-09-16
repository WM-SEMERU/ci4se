def write_file(self, filename, filetype, data):
    state = self.begin_transaction()
    try:
        directory = self.directory_class(self.header)
        self.get_directory(directory)
        dirent = directory.add_dirent(filename, filetype)
        data = to_numpy(data)
        sector_list = self.build_sectors(data)
        vtoc = self.get_vtoc_object()
        directory.save_dirent(self, dirent, vtoc, sector_list)
        self.write_sector_list(sector_list)
        self.write_sector_list(vtoc)
        self.write_sector_list(directory)
    except errors.AtrError:
        self.rollback_transaction(state)
        raise
    finally:
        self.get_metadata()