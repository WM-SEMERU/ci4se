def _set_catalog_view(self, session):
    if self._catalog_view == FEDERATED:
        try:
            session.use_federated_catalog_view()
        except AttributeError:
            pass
    else:
        try:
            session.use_isolated_catalog_view()
        except AttributeError:
            pass