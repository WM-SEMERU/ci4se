def update(driver_name, outputdir, version=None):
    platform = helpers.get_platform()
    driver_name = helpers.normalize_driver_name(driver_name)
    driver_class = helpers.get_driver_class(driver_name)
    driver = driver_class(outputdir, platform['os_name'], platform['os_bits'])
    if version:
        driver.download_driver_executable(version=version)
    elif driver.is_remote_higher_than_local():
        latest_remote_version = driver.get_latest_remote_version()
        driver.download_driver_executable(version=latest_remote_version)
    else:
        logger.info('{} is up to date'.format(driver_name))