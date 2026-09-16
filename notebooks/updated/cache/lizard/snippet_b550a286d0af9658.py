def append_result(self, results, num_matches):
    filename, lineno, colno, match_end, line = results
    if filename not in self.files:
        file_item = FileMatchItem(self, filename, self.sorting, self.text_color
            )
        file_item.setExpanded(True)
        self.files[filename] = file_item
        self.num_files += 1
    search_text = self.search_text
    title = "'%s' - " % search_text
    nb_files = self.num_files
    if nb_files == 0:
        text = _('String not found')
    else:
        text_matches = _('matches in')
        text_files = _('file')
        if nb_files > 1:
            text_files += 's'
        text = '%d %s %d %s' % (num_matches, text_matches, nb_files, text_files
            )
    self.set_title(title + text)
    file_item = self.files[filename]
    line = self.truncate_result(line, colno, match_end)
    item = LineMatchItem(file_item, lineno, colno, line, self.text_color)
    self.data[id(item)] = filename, lineno, colno