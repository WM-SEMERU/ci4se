def check_forbidden_filename(filename, destiny_os=os.name, restricted_names
    =restricted_names):
    return (filename in restricted_names or destiny_os == 'nt' and filename
        .split('.', 1)[0].upper() in nt_device_names)