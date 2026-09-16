def _get_model(self, lookup_keys, session):
    try:
        return self.queryset(session).filter_by(**lookup_keys).one()
    except NoResultFound:
        raise NotFoundException(
            'No model of type {0} was found using lookup_keys {1}'.format(
            self.model.__name__, lookup_keys))