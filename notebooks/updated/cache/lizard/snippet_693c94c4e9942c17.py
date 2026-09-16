def infofile_path(self):
    return os.path.normpath(os.path.join(self.dest_path, self.config.info_file)
        )