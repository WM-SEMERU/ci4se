def destructive_inject(self, filename, content):
    content = _unicode(content)
    backup_file(filename)
    full_path = self.__generate_file(filename)
    with codecs.open(full_path, 'r', encoding='utf-8') as f:
        new_content = self.inject_content(f.read(), content)
    with codecs.open(full_path, 'w+', encoding='utf-8') as f:
        f.write(new_content)