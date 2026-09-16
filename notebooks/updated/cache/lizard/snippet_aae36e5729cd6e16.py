def has_file_changed(directory, checksums, filetype='genbank'):
    pattern = NgdConfig.get_fileending(filetype)
    filename, expected_checksum = get_name_and_checksum(checksums, pattern)
    full_filename = os.path.join(directory, filename)
    if not os.path.isfile(full_filename):
        return True
    actual_checksum = md5sum(full_filename)
    return expected_checksum != actual_checksum