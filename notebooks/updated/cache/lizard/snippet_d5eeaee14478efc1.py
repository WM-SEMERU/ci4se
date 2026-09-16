def temp_copy(self):
    with contextmanagers.temp_dir() as temp_dir:
        temp_root_path = os.path.join(temp_dir, 'root')
        path = os.path.join(self.path, '')
        check_call(['rsync', '-r', '--exclude={}'.format(self.private_dir()
            ), '--filter=dir-merge,- {}'.format(self.ignore_patterns_file()
            ), path, temp_root_path])
        copy = self.__class__(path=temp_root_path)
        yield copy