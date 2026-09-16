def compress_and_upload(data, compressed_file, s3_path,
    multipart_chunk_size_mb=500, method='gz', delete=False, access_key=None,
    secret_key=None):
    logger = log.get_logger('s3')
    if all([access_key, secret_key]):
        configure(access_key=access_key, secret_key=secret_key, logger=logger)
    compress(data, compressed_file, fmt=method, logger=logger)
    put(compressed_file, s3_path, multipart_chunk_size_mb=
        multipart_chunk_size_mb, logger=logger)
    if delete:
        os.unlink(compressed_file)