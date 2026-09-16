def _get_firmware_file(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_name, file_ext = os.path.splitext(os.path.basename(filename))
            if file_ext in RAW_FIRMWARE_EXTNS:
                return os.path.join(dirpath, filename)