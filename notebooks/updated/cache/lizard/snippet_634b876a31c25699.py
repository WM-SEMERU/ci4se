def divine_format(text):
    try:
        nbformat.reads(text, as_version=4)
        return 'ipynb'
    except nbformat.reader.NotJSONError:
        pass
    lines = text.splitlines()
    for comment in (['', '#'] + _COMMENT_CHARS):
        metadata, _, _, _ = header_to_metadata_and_cell(lines, comment)
        ext = metadata.get('jupytext', {}).get('text_representation', {}).get(
            'extension')
        if ext:
            return ext[1:] + ':' + guess_format(text, ext)[0]
    for line in lines:
        if line == '```':
            return 'md'
    return 'py:' + guess_format(text, '.py')[0]