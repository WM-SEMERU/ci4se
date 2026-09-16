def process_file_object(file_obj, importer, progress):
    logging.info('Processing schedule data.')
    try:
        handler = XmlCallbacks(importer, progress)
        parser = sax.make_parser()
        parser.setContentHandler(handler)
        parser.setErrorHandler(handler)
        parser.parse(file_obj)
    except:
        logging.exception('Parse failed.')
        raise
    logging.info('Schedule data processed.')