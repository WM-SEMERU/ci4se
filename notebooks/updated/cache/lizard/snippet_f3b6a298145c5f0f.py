def alias_family(self, family_id, alias_id):
    if self._catalog_session is not None:
        return self._catalog_session.alias_catalog(catalog_id=family_id,
            alias_id=alias_id)
    self._alias_id(primary_id=family_id, equivalent_id=alias_id)