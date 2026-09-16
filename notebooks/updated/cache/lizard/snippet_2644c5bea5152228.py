def get_mail_keys(message, complete=True):
    if complete:
        log.debug('Get all headers')
        all_headers_keys = {i.lower() for i in message.keys()}
        all_parts = ADDRESSES_HEADERS | OTHERS_PARTS | all_headers_keys
    else:
        log.debug('Get only mains headers')
        all_parts = ADDRESSES_HEADERS | OTHERS_PARTS
    log.debug('All parts to get: {}'.format(', '.join(all_parts)))
    return all_parts