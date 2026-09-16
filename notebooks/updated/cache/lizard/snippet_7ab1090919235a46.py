def set_config(path):
    logging.info('LOADING FROM: {}'.format(path))
    session.config = load_config(path)
    return session.config