def from_file_path(cls, path_prefix):
    with cls._path_prefix_to_files(path_prefix, 'r') as (array_file, vocab_file
        ):
        return cls.from_files(array_file, vocab_file)