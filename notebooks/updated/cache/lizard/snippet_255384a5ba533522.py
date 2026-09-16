def extract_references_from_wets(wet_files, metadata_dir, out_dir, tmp_dir=None
    ):
    shard_files = make_ref_shard_files(out_dir)
    num_refs = 0
    for i, wet_file in enumerate(wet_files):
        num_refs_in_wet = 0
        tf.logging.info('Processing file %d', i)
        metadata_fname = os.path.join(metadata_dir, os.path.basename(wet_file)
            ) + cc_utils.METADTA_SUFFIX
        with tf.gfile.Open(cc_utils.readahead(metadata_fname)) as f:
            wet_metadata = json.loads(f.read())
        if not wet_metadata:
            continue
        if wet_file.startswith('http'):
            if not tmp_dir:
                tmp_dir = tempfile.gettempdir()
            record_gen = cc_utils.wet_records_from_url(wet_file, tmp_dir)
        else:
            record_gen = cc_utils.wet_records_from_file_obj(cc_utils.
                gzip_memfile(wet_file), take_ownership=True)
        for wet_record in record_gen:
            shard_ids = wet_metadata.get(wet_record.url)
            if not shard_ids:
                continue
            ex = _make_example_from_record(wet_record)
            ex_str = ex.SerializeToString()
            for shard_id in shard_ids:
                shard_files[shard_id].write(ex_str)
            num_refs += 1
            num_refs_in_wet += 1
        tf.logging.info('Wrote out %d references for this WET', num_refs_in_wet
            )
    tf.logging.info('Wrote out %d references total', num_refs)
    for shard_file in shard_files:
        shard_file.close()