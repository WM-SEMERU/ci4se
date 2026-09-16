def WriteVcard(filename, vcard, fopen=codecs.open):
    if os.access(filename, os.F_OK):
        logger.warning('File exists at "{}", skipping.'.format(filename))
        return False
    try:
        with fopen(filename, 'w', encoding='utf-8') as f:
            logger.debug('Writing {}:\n{}'.format(filename, u(vcard.
                serialize())))
            f.write(u(vcard.serialize()))
    except OSError:
        logger.error('Error writing to file "{}", skipping.'.format(filename))
        return False
    return True