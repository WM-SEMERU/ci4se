def init_write_index(es_write, es_write_index):
    logging.info('Initializing index: ' + es_write_index)
    es_write.indices.delete(es_write_index, ignore=[400, 404])
    es_write.indices.create(es_write_index, body=MAPPING_GIT)