def worker(url_key, property_name, function, function_arguments):
    error_msg = None
    try:
        data = function(*function_arguments)
    except Exception as e:
        data = []
        error_msg = 'Error: ' + traceback.format_exc().strip()
        error_msg += '\n' + str(e.message)
    if error_msg:
        logger.error(error_msg)
        error_msg = None
    func_name = str(function.__name__)
    logger.info('Attempting to save output from `%s`.' % func_name)
    return _save_to_database(url=url_key, property_name=property_name, data
        =data)