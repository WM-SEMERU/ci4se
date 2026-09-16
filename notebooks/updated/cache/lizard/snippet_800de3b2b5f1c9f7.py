def assort_files(self, candidates):
    by_ext = defaultdict(list)
    for path in candidates:
        by_ext[split_extension(path)[1].lower()].append(path)
    try:
        primary_file = by_ext[self.ext]
    except KeyError:
        raise ArcanaFileFormatError(
            'No files match primary file extension of {} out of potential candidates of {}'
            .format(self, "', '".join(candidates)))
    if not primary_file:
        raise ArcanaFileFormatError('No potential files for primary file of {}'
            .format(self))
    elif len(primary_file) > 1:
        raise ArcanaFileFormatError(
            "Multiple potential files for '{}' primary file of {}".format(
            "', '".join(primary_file), self))
    else:
        primary_file = primary_file[0]
    aux_files = {}
    for aux_name, aux_ext in self.aux_files.items():
        try:
            aux = by_ext[aux_ext]
        except KeyError:
            raise ArcanaFileFormatError(
                "No files match auxiliary file extension '{}' of {} out of potential candidates of {}"
                .format(aux_ext, self, "', '".join(candidates)))
        if len(aux) > 1:
            raise ArcanaFileFormatError(
                "Multiple potential files for '{}' auxiliary file ext. ({}) of {}"
                .format("', '".join(aux), self))
        aux_files[aux_name] = aux[0]
    return primary_file, aux_files