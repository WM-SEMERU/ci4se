def create_epub(self, output_directory, epub_name=None):

    def createTOCs_and_ContentOPF():
        for epub_file, name in ((self.toc_html, 'toc.html'), (self.toc_ncx,
            'toc.ncx'), (self.opf, 'content.opf')):
            epub_file.add_chapters(self.chapters)
            epub_file.write(os.path.join(self.OEBPS_DIR, name))

    def create_zip_archive(epub_name):
        try:
            assert isinstance(epub_name, basestring) or epub_name is None
        except AssertionError:
            raise TypeError('epub_name must be string or None')
        if epub_name is None:
            epub_name = self.title
        epub_name = ''.join([c for c in epub_name if c.isalpha() or c.
            isdigit() or c == ' ']).rstrip()
        epub_name_with_path = os.path.join(output_directory, epub_name)
        try:
            os.remove(os.path.join(epub_name_with_path, '.zip'))
        except OSError:
            pass
        shutil.make_archive(epub_name_with_path, 'zip', self.EPUB_DIR)
        return epub_name_with_path + '.zip'

    def turn_zip_into_epub(zip_archive):
        epub_full_name = zip_archive.strip('.zip') + '.epub'
        try:
            os.remove(epub_full_name)
        except OSError:
            pass
        os.rename(zip_archive, epub_full_name)
        return epub_full_name
    createTOCs_and_ContentOPF()
    epub_path = turn_zip_into_epub(create_zip_archive(epub_name))
    return epub_path