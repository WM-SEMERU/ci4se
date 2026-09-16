def read_lines_from_file(cls_name, filename):
    with tf.io.gfile.GFile(filename, 'rb') as f:
        lines = [tf.compat.as_text(line)[:-1] for line in f]
    header_line = '%s%s' % (_HEADER_PREFIX, cls_name)
    if lines[0] != header_line:
        raise ValueError(
            'File {fname} does not seem to have been created from {name}.save_to_file.'
            .format(fname=filename, name=cls_name))
    metadata_dict = json.loads(lines[1][len(_METADATA_PREFIX):])
    return lines[2:], metadata_dict