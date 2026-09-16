def __get_indexer(in_fns, selected_type=None):
    indexer = None
    if selected_type is not None:
        indexer = get_indexer_by_filetype(selected_type)
    elif len(in_fns) == 0:
        raise IndexError('reading from stdin, unable to guess input file ' +
            """type, use -t option to set manually.
""")
    else:
        extension = set([os.path.splitext(f)[1] for f in in_fns])
        assert len(extension) >= 1
        if len(extension) > 1:
            raise IndexError(
                'more than one file extension present, unable ' +
                """to get input type, use -t option to set manually.
""")
        else:
            indexer = get_indexer_by_file_extension(list(extension)[0])
    assert indexer is not None
    return indexer