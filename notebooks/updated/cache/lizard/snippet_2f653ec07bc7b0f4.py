def iter_grants(self, as_json=True):
    records = self.client.ListRecords(metadataPrefix='oaf', set=self.setspec)
    for rec in records:
        try:
            grant_out = rec.raw
            if as_json:
                grant_out = self.grantxml2json(grant_out)
            yield grant_out
        except FunderNotFoundError as e:
            current_app.logger.warning("Funder '{0}' not found.".format(e.
                funder_id))