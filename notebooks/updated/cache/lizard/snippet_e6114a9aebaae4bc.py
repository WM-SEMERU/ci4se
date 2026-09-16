def clean(outputdir, drivers=None):
    if drivers:
        drivers_split = [helpers.split_driver_name_and_version(x) for x in
            drivers]
        file_data = [(helpers.normalize_driver_name(x[0]), x[1]) for x in
            drivers_split]
    else:
        file_data = [(x, None) for x in config.ALL_DRIVERS]
    files = [file for file in os.listdir(outputdir) if os.path.isfile(os.
        path.join(outputdir, file))]
    for file in files:
        for data in file_data:
            prefix, version = data
            starts_with = file.startswith(prefix)
            version_match = 'N/A'
            if version is not None:
                file_version = helpers.extract_version_from_filename(file)
                if file_version == version:
                    version_match = True
                else:
                    version_match = False
            if starts_with and version_match in [True, 'N/A']:
                filepath = os.path.join(outputdir, file)
                try:
                    os.remove(filepath)
                except OSError:
                    pass
                finally:
                    logger.info('removed {}'.format(file))
                    break