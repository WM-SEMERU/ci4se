def in_noninjected_file(self, file_path, content):
    if os.path.exists(file_path):
        file_content = codecs.open(file_path, encoding='utf-8').read()
        file_content = self.wrapper_match.sub('', file_content)
    else:
        file_content = ''
    return file_content.find(content) != -1