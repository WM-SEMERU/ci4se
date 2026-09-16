def process_firehose_archive(bucket, key):
    data = {}
    with tempfile.NamedTemporaryFile(mode='w+b') as fh:
        s3.download_file(bucket, key, fh.name)
        log.warning('Downloaded Key Size:%s Key:%s', sizeof_fmt(os.path.
            getsize(fh.name)), key)
        fh.seek(0, 0)
        record_count = 0
        iteration_count = 0
        for r in records_iter(gzip.GzipFile(fh.name, mode='r')):
            record_count += len(r['logEvents'])
            iteration_count += 1
            key = '%s/%s/%s' % (r['owner'], r['logGroup'], r['logStream'])
            data.setdefault(key, []).extend(r['logEvents'])
            if record_count > EVENTS_SIZE_BUFFER:
                log.warning('Incremental Data Load records:%d enis:%d',
                    record_count, len(data))
                for k in data:
                    process_record_set(k, data[k])
                data.clear()
                gc.collect()
                record_count = 0
        for k in data:
            process_record_set(k, data[k])
        data.clear()
        gc.collect()