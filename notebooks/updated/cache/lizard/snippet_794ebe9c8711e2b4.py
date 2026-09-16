def defaults(self):
    return dict(access_right='open', description=self.description, license=
        'other-open', publication_date=self.release['published_at'][:10],
        related_identifiers=list(self.related_identifiers), version=self.
        version, title=self.title, upload_type='software')