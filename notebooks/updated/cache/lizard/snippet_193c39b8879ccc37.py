def write_file(file_name, file_contents, indent=None):
    make_dir(os.path.dirname(file_name))
    if isinstance(file_contents, string_types):
        text_to_write = file_contents
    else:
        text_to_write = json.dumps(file_contents, sort_keys=True, indent=indent
            )
    with codecs.open(file_name, 'w', encoding='utf-8') as out_file:
        out_file.write(text_to_write)