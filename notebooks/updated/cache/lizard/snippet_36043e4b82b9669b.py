def _split_source_page(self, path):
    with codecs.open(path, 'rb', 'utf-8') as fd:
        textlist = fd.readlines()
    metadata_notation = '---\n'
    if textlist[0] != metadata_notation:
        logging.error('{} first line must be triple-dashed!'.format(path))
        sys.exit(1)
    metadata_textlist = []
    metadata_end_flag = False
    idx = 1
    max_idx = len(textlist)
    while not metadata_end_flag:
        metadata_textlist.append(textlist[idx])
        idx += 1
        if idx >= max_idx:
            logging.error("{} doesn't have end triple-dashed!".format(path))
            sys.exit(1)
        if textlist[idx] == metadata_notation:
            metadata_end_flag = True
    content = textlist[idx + 1:]
    return metadata_textlist, content