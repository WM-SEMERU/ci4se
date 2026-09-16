def convert_verse_group_elements(self):
    for verse_group in self.main.getroot().findall('.//verse-group'):
        label = verse_group.find('label')
        title = verse_group.find('title')
        subtitle = verse_group.find('subtitle')
        verse_group.tag = 'div'
        verse_group.attrib['id'] = 'verse-group'
        if label is not None or title is not None or subtitle is not None:
            new_verse_title = etree.Element('b')
            verse_group.insert(0, new_verse_title)
            if label is not None:
                append_all_below(new_verse_title, label)
                remove(label)
            if title is not None:
                append_all_below(new_verse_title, title)
                remove(title)
            if subtitle is not None:
                append_all_below(new_verse_title, subtitle)
                remove(subtitle)
        for verse_line in verse_group.findall('verse-line'):
            verse_line.tag = 'p'
            verse_line.attrib['class'] = 'verse-line'