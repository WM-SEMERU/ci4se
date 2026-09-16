def print_dict(dict_name, dict_value, logger: Logger=None):
    if logger is None:
        print(dict_name + ' = ')
        try:
            from pprint import pprint
            pprint(dict_value)
        except:
            print(dict_value)
    else:
        logger.info(dict_name + ' = ')
        try:
            from pprint import pformat
            logger.info(pformat(dict_value))
        except:
            logger.info(dict_value)