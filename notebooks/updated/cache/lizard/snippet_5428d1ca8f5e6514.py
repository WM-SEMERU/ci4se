def apply(db, op):
    dbname = op['ns'].split('.')[0] or 'admin'
    opts = bson.CodecOptions(uuid_representation=bson.binary.STANDARD)
    db[dbname].command('applyOps', [op], codec_options=opts)