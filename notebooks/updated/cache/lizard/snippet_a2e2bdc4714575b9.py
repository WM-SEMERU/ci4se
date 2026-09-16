def add_chapter(self, c):
    try:
        assert type(c) == chapter.Chapter
    except AssertionError:
        raise TypeError('chapter must be of type Chapter')
    chapter_file_output = os.path.join(self.OEBPS_DIR, self.
        current_chapter_path)
    c._replace_images_in_chapter(self.OEBPS_DIR)
    c.write(chapter_file_output)
    self._increase_current_chapter_number()
    self.chapters.append(c)