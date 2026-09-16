def has_parent_objective_banks(self, objective_bank_id):
    if self._catalog_session is not None:
        return self._catalog_session.has_parent_catalogs(catalog_id=
            objective_bank_id)
    return self._hierarchy_session.has_parents(id_=objective_bank_id)