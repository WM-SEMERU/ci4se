def csvdiff_cmd(index_columns, from_csv, to_csv, style=None, output=None,
    sep=',', quiet=False, ignore_columns=None, significance=None):
    if ignore_columns is not None:
        for i in ignore_columns:
            if i in index_columns:
                error.abort("You can't ignore an index column")
    ostream = open(output, 'w') if output else io.StringIO(
        ) if quiet else sys.stdout
    try:
        if style == 'summary':
            _diff_and_summarize(from_csv, to_csv, index_columns, ostream,
                sep=sep, ignored_columns=ignore_columns, significance=
                significance)
        else:
            compact = style == 'compact'
            _diff_files_to_stream(from_csv, to_csv, index_columns, ostream,
                compact=compact, sep=sep, ignored_columns=ignore_columns,
                significance=significance)
    except records.InvalidKeyError as e:
        error.abort(e.args[0])
    finally:
        ostream.close()