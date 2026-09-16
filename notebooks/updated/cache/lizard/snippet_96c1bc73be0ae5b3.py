def get_title(self, article):
    title = ''
    doc = article.doc
    title_element = self.parser.getElementsByTag(doc, tag='title')
    if title_element is None or len(title_element) == 0:
        return title
    title_text = self.parser.getText(title_element[0])
    used_delimeter = False
    if '|' in title_text:
        title_text = self.split_title(title_text, PIPE_SPLITTER)
        used_delimeter = True
    if not used_delimeter and '-' in title_text:
        title_text = self.split_title(title_text, DASH_SPLITTER)
        used_delimeter = True
    if not used_delimeter and '»' in title_text:
        title_text = self.split_title(title_text, ARROWS_SPLITTER)
        used_delimeter = True
    if not used_delimeter and ':' in title_text:
        title_text = self.split_title(title_text, COLON_SPLITTER)
        used_delimeter = True
    title = MOTLEY_REPLACEMENT.replaceAll(title_text)
    return title