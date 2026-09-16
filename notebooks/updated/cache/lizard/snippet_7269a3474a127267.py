def add_init_files(path, zip_handler):
    paths = path.split('\\')
    paths = paths[:len(paths) - 1]
    for sub_path in paths:
        for root, dirs, files in os.walk(sub_path):
            for file_to_zip in [x for x in files if '__init__.py' in x]:
                filename = os.path.join(root, file_to_zip)
                zip_con = filename.replace('\\', '/')
                if zip_con in zip_handler.namelist():
                    continue
                add_file(filename, zip_handler, False)