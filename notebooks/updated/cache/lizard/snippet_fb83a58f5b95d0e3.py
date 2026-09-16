def find_matlab_version(process_path):
    bin_path = os.path.dirname(process_path)
    matlab_path = os.path.dirname(bin_path)
    matlab_dir_name = os.path.basename(matlab_path)
    version = matlab_dir_name
    if not is_linux():
        version = matlab_dir_name.replace('MATLAB_', '').replace('.app', '')
    if not is_valid_release_version(version):
        return None
    return version