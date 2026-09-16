def affiliation_history(self):
    aff_ids = [e.attrib.get('affiliation-id') for e in self.xml.findall(
        'author-profile/affiliation-history/affiliation') if e is not None and
        len(list(e.find('ip-doc').iter())) > 1]
    return [ScopusAffiliation(aff_id) for aff_id in aff_ids]