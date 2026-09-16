def serializeCitation(self):
    citation_details = []
    citation_id = tethnedao.getMaxCitationID()
    for citation in self.corpus.features['citations'].index.values():
        date_match = re.search('(\\d+)', citation)
        if date_match is not None:
            date = date_match.group(1)
        if date_match is None:
            date_match = re.search('NONE', citation)
            date = date_match.group()
        first_author = citation.replace('_', ' ').split(date)[0].rstrip()
        journal = citation.replace('_', ' ').split(date)[1].lstrip()
        citation_key = citation
        if citation_key not in self.citationIdMap:
            citation_id += 1
            self.citationIdMap[citation_key] = citation_id
            citation_data = {'model': 'django-tethne.citation', 'pk':
                citation_id, 'fields': {'literal': citation, 'journal':
                journal, 'first_author': first_author, 'date': date}}
            citation_details.append(citation_data)
    return citation_details