def display_ioc(self, width=120, sep='  ', params=False):
    s = 'Name: {}\n'.format(self.metadata.findtext('short_description',
        default='No Name'))
    s += 'ID: {}\n'.format(self.root.attrib.get('id'))
    s += 'Created: {}\n'.format(self.metadata.findtext('authored_date',
        default='No authored_date'))
    s += 'Updated: {}\n\n'.format(self.root.attrib.get('last-modified',
        default='No last-modified attrib'))
    s += 'Author: {}\n'.format(self.metadata.findtext('authored_by',
        default='No authored_by'))
    desc = self.metadata.findtext('description', default='No Description')
    desc = textwrap.wrap(desc, width=width)
    desc = '\n'.join(desc)
    s += 'Description:\n{}\n\n'.format(desc)
    links = self.link_text()
    if links:
        s += '{}'.format(links)
    content_text = self.criteria_text(sep=sep, params=params)
    s += '\nCriteria:\n{}'.format(content_text)
    return s