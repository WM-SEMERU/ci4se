def is_package(self, fullname):
    filename = os.path.split(self.get_filename(fullname))[1]
    filename_base = filename.rsplit('.', 1)[0]
    tail_name = fullname.rpartition('.')[2]
    return filename_base == '__init__' and tail_name != '__init__'