def download_and_extract(path, url, input_filename, target_filename):
    logging.info('Downloading and extracting data to: %s' % path)
    input_file = find_file(path, input_filename)
    target_file = find_file(path, target_filename)
    if input_file and target_file:
        logging.info('Already downloaded and extracted %s.' % url)
        return input_file, target_file
    compressed_file = download_from_url(path, url)
    logging.info('Extracting %s.' % compressed_file)
    with tarfile.open(compressed_file, 'r:gz') as corpus_tar:
        corpus_tar.extractall(path)
    input_file = find_file(path, input_filename)
    target_file = find_file(path, target_filename)
    if input_file and target_file:
        return input_file, target_file
    raise OSError('Download/extraction failed for url %s to path %s' % (url,
        path))