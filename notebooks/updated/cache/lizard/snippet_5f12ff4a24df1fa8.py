def get_package_data(filename, mode='rb'):
    if os.path.exists(filename):
        with open(filename, mode=mode) as in_file:
            return in_file.read()
    else:
        parts = os.path.normpath(filename).split(os.sep)
        for part, index in zip(parts, range(len(parts))):
            if part.endswith('.zip'):
                zip_path = os.sep.join(parts[:index + 1])
                member_path = os.sep.join(parts[index + 1:])
                break
        if platform.system() == 'Windows':
            member_path = member_path.replace('\\', '/')
        with zipfile.ZipFile(zip_path) as zip_file:
            return zip_file.read(member_path)