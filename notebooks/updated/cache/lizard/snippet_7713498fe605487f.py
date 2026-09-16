def validate_one(func_name):
    doc = Docstring(func_name)
    errs, wrns, examples_errs = get_validation_data(doc)
    return {'type': doc.type, 'docstring': doc.clean_doc, 'deprecated': doc
        .deprecated, 'file': doc.source_file_name, 'file_line': doc.
        source_file_def_line, 'github_link': doc.github_url, 'errors': errs,
        'warnings': wrns, 'examples_errors': examples_errs}