def file_copy(filename, settings):
    for k, v in settings.items():
        if k.startswith('dest'):
            shutil.copyfile(filename, v)