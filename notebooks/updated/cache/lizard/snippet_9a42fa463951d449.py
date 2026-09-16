def matches(self, fileset):
    if fileset._resource_name is not None:
        return fileset._resource_name in self.resource_names(fileset.
            repository.type)
    elif self.directory:
        if op.isdir(fileset.path):
            if self.within_dir_exts is None:
                return True
            else:
                return self.within_dir_exts == frozenset(split_extension(f)
                    [1] for f in os.listdir(fileset.path) if not f.
                    startswith('.'))
        else:
            return False
    elif op.isfile(fileset.path):
        all_paths = [fileset.path] + fileset._potential_aux_files
        try:
            primary_path = self.assort_files(all_paths)[0]
        except ArcanaFileFormatError:
            return False
        else:
            return primary_path == fileset.path
    else:
        return False