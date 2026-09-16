def is_published(self):
    citeable = 'publication_info' in self.record and is_citeable(self.
        record['publication_info'])
    submitted = 'dois' in self.record and any('journal_title' in el for el in
        force_list(self.record.get('publication_info')))
    return citeable or submitted