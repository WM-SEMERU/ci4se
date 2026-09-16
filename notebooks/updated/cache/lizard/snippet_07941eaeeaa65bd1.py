def index_objects(mapping_type, ids, chunk_size=100, es=None, index=None):
    if settings.ES_DISABLED:
        return
    log.debug('Indexing objects {0}-{1}. [{2}]'.format(ids[0], ids[-1], len
        (ids)))
    model = mapping_type.get_model()
    for id_list in chunked(ids, chunk_size):
        documents = []
        for obj in model.objects.filter(id__in=id_list):
            try:
                documents.append(mapping_type.extract_document(obj.id, obj))
            except Exception as exc:
                log.exception('Unable to extract document {0}: {1}'.format(
                    obj, repr(exc)))
        if documents:
            mapping_type.bulk_index(documents, id_field='id', es=es, index=
                index)