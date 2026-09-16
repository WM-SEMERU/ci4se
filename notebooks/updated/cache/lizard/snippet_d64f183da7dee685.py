def write_or_delete_file(self, what, filename, data, force=False):
    if data:
        self.write_file(what, filename, data)
    elif os.path.exists(filename):
        if data is None and not force:
            log.warn('%s not set in setup(), but %s exists', what, filename)
            return
        else:
            self.delete_file(filename)