def get_temporary_filename(extension='', use_program_temp_dir=True):
    dir_name = None
    if use_program_temp_dir:
        dir_name = program_temp_directory
    tmp_output_file = tempfile.NamedTemporaryFile(delete=False, prefix=
        temp_file_prefix, suffix=extension, dir=dir_name, mode='wb')
    tmp_output_file.close()
    return tmp_output_file.name