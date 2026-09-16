def read_content(self):
    if self.is_directory():
        data = get_index_html(get_files(self.get_os_filename()))
        if isinstance(data, unicode):
            data = data.encode('iso8859-1', 'ignore')
    else:
        data = super(FileUrl, self).read_content()
    return data