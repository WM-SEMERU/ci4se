def cite(self, max_authors=5):
    citation_data = {'title': self.title, 'authors': self.authors_et_al(
        max_authors), 'year': self.year, 'journal': self.journal, 'volume':
        self.volume, 'issue': self.issue, 'pages': self.pages}
    citation = '{authors} ({year}). {title} {journal}'.format(**citation_data)
    if self.volume and self.issue and self.pages:
        citation += ' {volume}({issue}): {pages}.'.format(**citation_data)
    elif self.volume and self.issue:
        citation += ' {volume}({issue}).'.format(**citation_data)
    elif self.volume and self.pages:
        citation += ' {volume}: {pages}.'.format(**citation_data)
    elif self.volume:
        citation += ' {volume}.'.format(**citation_data)
    elif self.pages:
        citation += ' {pages}.'.format(**citation_data)
    else:
        citation += '.'
    return citation