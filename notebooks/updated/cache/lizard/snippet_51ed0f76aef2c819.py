def _CheckLogFileSize(cursor):
    innodb_log_file_size = int(_ReadVariable('innodb_log_file_size', cursor))
    required_size = 10 * mysql_blobs.BLOB_CHUNK_SIZE
    if innodb_log_file_size < required_size:
        max_blob_size = innodb_log_file_size / 10
        max_blob_size_mib = max_blob_size / 2 ** 20
        logging.warning(
            'MySQL innodb_log_file_size of %d is required, got %d. Storing Blobs bigger than %.4f MiB will fail.'
            , required_size, innodb_log_file_size, max_blob_size_mib)