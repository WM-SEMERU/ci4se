def make_heading_authors(self, authors):
    author_element = etree.Element('h3', {'class': 'authors'})
    first = True
    for author in authors:
        if first:
            first = False
        else:
            append_new_text(author_element, ',', join_str='')
        collab = author.find('collab')
        anon = author.find('anon')
        if collab is not None:
            append_all_below(author_element, collab)
        elif anon is not None:
            append_new_text(author_element, 'Anonymous')
        else:
            author_name, _ = self.get_contrib_names(author)
            append_new_text(author_element, author_name)
        first = True
        for xref in author.xpath(
            "./xref[@ref-type='corresp' or @ref-type='aff']"):
            _sup = xref.find('sup')
            sup_text = all_text(_sup) if _sup is not None else ''
            auth_sup = etree.SubElement(author_element, 'sup')
            sup_link = etree.SubElement(auth_sup, 'a', {'href': self.
                main_fragment.format(xref.attrib['rid'])})
            sup_link.text = sup_text
            if first:
                first = False
            else:
                append_new_text(auth_sup, ', ', join_str='')
    return author_element