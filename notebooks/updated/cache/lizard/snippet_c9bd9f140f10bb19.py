def from_source(cls, filename, args=None, unsaved_files=None, options=0,
    index=None):
    if args is None:
        args = []
    if unsaved_files is None:
        unsaved_files = []
    if index is None:
        index = Index.create()
    args_array = None
    if len(args) > 0:
        args_array = (c_char_p * len(args))(*[b(x) for x in args])
    unsaved_array = None
    if len(unsaved_files) > 0:
        unsaved_array = (_CXUnsavedFile * len(unsaved_files))()
        for i, (name, contents) in enumerate(unsaved_files):
            if hasattr(contents, 'read'):
                contents = contents.read()
            unsaved_array[i].name = b(name)
            unsaved_array[i].contents = b(contents)
            unsaved_array[i].length = len(contents)
    ptr = conf.lib.clang_parseTranslationUnit(index, filename, args_array,
        len(args), unsaved_array, len(unsaved_files), options)
    if not ptr:
        raise TranslationUnitLoadError('Error parsing translation unit.')
    return cls(ptr, index=index)