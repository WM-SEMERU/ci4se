def load_into_collections_from_zipfile(collections, zipfile):
    with ZipFile(zipfile) as zipf:
        names = zipf.namelist()
        name_map = dict([(os.path.splitext(name)[0], index) for index, name in
            enumerate(names)])
        for coll in collections:
            coll_name = get_collection_name(coll)
            index = name_map.get(coll_name)
            if index is None:
                continue
            coll_fn = names[index]
            ext = os.path.splitext(coll_fn)[1]
            try:
                content_type = MimeTypeRegistry.get_type_for_extension(ext)
            except KeyError:
                raise ValueError(
                    'Could not infer MIME type for file extension "%s".' % ext)
            coll_data = DecodingStream(zipf.open(coll_fn, 'r'))
            load_into_collection_from_stream(coll, coll_data, content_type)