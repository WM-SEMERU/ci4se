def read_html_file(data_dir, fileroot, encoding=None):
    fname = os.path.join(data_dir, RAW_HTML_DIRNAME, fileroot + RAW_HTML_EXT)
    encodings = (encoding,) if encoding else ('utf-8', 'iso-8859-1')
    for encoding in encodings:
        try:
            with io.open(fname, mode='rt', encoding=encoding) as f:
                raw_html = f.read()
            break
        except (UnicodeDecodeError, UnicodeError):
            raw_html = None
    return ftfy.fix_encoding(raw_html).strip()