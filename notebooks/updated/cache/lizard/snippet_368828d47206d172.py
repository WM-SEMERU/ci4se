def pretty_print_device(device):
    logging.info('Device Instance ID: %s' % device['id'])
    if 'nickname' in device:
        logging.info('    Nickname: %s' % device['nickname'])
    if 'modelId' in device:
        logging.info('    Model: %s' % device['modelId'])
    logging.info('')