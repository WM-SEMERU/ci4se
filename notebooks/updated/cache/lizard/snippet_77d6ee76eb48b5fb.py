def convert(self):
    if not os.path.exists(os.path.dirname(self.file_generator.to_path)):
        dirname = os.path.dirname(self.file_generator.to_path)
        if dirname:
            os.makedirs(dirname)
    if os.path.isdir(self.file_generator.from_path):
        self._many_to_many()
    elif os.path.isfile(self.file_generator.from_path
        ) or fileio.GenericFilePath.is_url(self.file_generator.from_path):
        if self.file_generator.from_path_compression in ('zip', 'tar',
            'tar.gz', 'tar.bz2'):
            self._many_to_many()
        elif self.file_generator.from_path_compression in ('gz', 'bz2'):
            self._one_to_one()
        elif not self.file_generator.from_path_compression:
            self._one_to_one()
    elif self.file_generator.from_path.isdigit():
        self._one_to_one()
    else:
        raise TypeError('Unknown input file format: "{}"'.format(self.
            file_generator.from_path))