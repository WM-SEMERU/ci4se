def try_opening_file(self):
    if os.path.isfile(self.path):
        self.file = open(self.path, 'r')
        self.file_is_opened = True