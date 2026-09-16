def _parse_czeng(*paths, **kwargs):
    filter_path = kwargs.get('filter_path', None)
    if filter_path:
        re_block = re.compile('^[^-]+-b(\\d+)-\\d\\d[tde]')
        with tf.io.gfile.GFile(filter_path) as f:
            bad_blocks = {blk for blk in re.search('qw{([\\s\\d]*)}', f.
                read()).groups()[0].split()}
        logging.info(
            'Loaded %d bad blocks to filter from CzEng v1.6 to make v1.7.',
            len(bad_blocks))
    for path in paths:
        for gz_path in tf.io.gfile.glob(path):
            with tf.io.gfile.GFile(gz_path, 'rb') as g, gzip.GzipFile(fileobj=g
                ) as f:
                for line in f:
                    line = line.decode('utf-8')
                    if not line.strip():
                        continue
                    id_, unused_score, cs, en = line.split('\t')
                    if filter_path:
                        block_match = re.match(re_block, id_)
                        if block_match and block_match.groups()[0
                            ] in bad_blocks:
                            continue
                    yield {'cs': cs.strip(), 'en': en.strip()}