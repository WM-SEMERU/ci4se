def get_introspection_data(cls, tax_benefit_system):
    comments = inspect.getcomments(cls)
    try:
        absolute_file_path = inspect.getsourcefile(cls)
    except TypeError:
        source_file_path = None
    else:
        source_file_path = absolute_file_path.replace(tax_benefit_system.
            get_package_metadata()['location'], '')
    try:
        source_lines, start_line_number = inspect.getsourcelines(cls)
        source_code = textwrap.dedent(''.join(source_lines))
    except (IOError, TypeError):
        source_code, start_line_number = None, None
    return comments, source_file_path, source_code, start_line_number