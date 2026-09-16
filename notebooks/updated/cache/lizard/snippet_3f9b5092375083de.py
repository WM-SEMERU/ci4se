def html_header():
    file_path = resources_path('header.html')
    with codecs.open(file_path, 'r', encoding='utf8') as header_file:
        content = header_file.read()
        content = content.replace('PATH', resources_path())
    return content