def _do_subst(node, subs):
    contents = node.get_text_contents()
    if subs:
        for k, val in subs:
            contents = re.sub(k, val, contents)
    if 'b' in TEXTFILE_FILE_WRITE_MODE:
        try:
            contents = bytearray(contents, 'utf-8')
        except UnicodeDecodeError:
            contents = bytearray(contents)
    return contents