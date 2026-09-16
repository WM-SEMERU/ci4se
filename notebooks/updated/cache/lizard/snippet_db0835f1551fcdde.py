def from_files(cls, files_to_sort, reader=None, **kwargs):
    from satpy.readers import group_files
    file_groups = group_files(files_to_sort, reader=reader, **kwargs)
    scenes = (Scene(filenames=fg) for fg in file_groups)
    return cls(scenes)