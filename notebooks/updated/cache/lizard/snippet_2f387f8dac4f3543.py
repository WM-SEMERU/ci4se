def file_in_confined_directories(filepath, confined_directories):
    securesystemslib.formats.RELPATH_SCHEMA.check_match(filepath)
    securesystemslib.formats.RELPATHS_SCHEMA.check_match(confined_directories)
    for confined_directory in confined_directories:
        if confined_directory == '':
            return True
        filepath = os.path.normpath(filepath)
        confined_directory = os.path.normpath(confined_directory)
        if os.path.dirname(filepath) == confined_directory:
            return True
    return False