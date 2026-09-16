def OpenFileEntry(cls, path_spec_object, resolver_context=None):
    file_system = cls.OpenFileSystem(path_spec_object, resolver_context=
        resolver_context)
    if resolver_context is None:
        resolver_context = cls._resolver_context
    file_entry = file_system.GetFileEntryByPathSpec(path_spec_object)
    resolver_context.ReleaseFileSystem(file_system)
    return file_entry