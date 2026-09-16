def get_driver(driver='ASCII_RS232', *args, **keywords):
    if driver.upper() == 'ASCII_RS232':
        return drivers.ASCII_RS232(*args, **keywords)
    else:
        raise NotImplementedError('Driver not supported: ' + str(driver))