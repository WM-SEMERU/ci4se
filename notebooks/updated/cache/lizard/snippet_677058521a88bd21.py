def osu_run1(data_set='osu_run1', sample_every=4):
    path = os.path.join(data_path, data_set)
    if not data_available(data_set):
        import zipfile
        download_data(data_set)
        zip = zipfile.ZipFile(os.path.join(data_path, data_set,
            'run1TXT.ZIP'), 'r')
        for name in zip.namelist():
            zip.extract(name, path)
    from . import mocap
    Y, connect = mocap.load_text_data('Aug210106', path)
    Y = Y[0:-1:sample_every, :]
    return data_details_return({'Y': Y, 'connect': connect}, data_set)