def paired_paths(main_path, fmt, formats):
    if not formats:
        return [(main_path, {'extension': os.path.splitext(main_path)[1]})]
    formats = long_form_multiple_formats(formats)
    base = base_path(main_path, fmt)
    paths = [full_path(base, fmt) for fmt in formats]
    if main_path not in paths:
        raise InconsistentPath(
            "Paired paths '{}' do not include the current notebook path '{}'. Current format is '{}', and paired formats are '{}'."
            .format("','".join(paths), main_path, short_form_one_format(fmt
            ), short_form_multiple_formats(formats)))
    if len(paths) > len(set(paths)):
        raise InconsistentPath(
            'Duplicate paired paths for this notebook. Please fix jupytext.formats.'
            )
    return list(zip(paths, formats))