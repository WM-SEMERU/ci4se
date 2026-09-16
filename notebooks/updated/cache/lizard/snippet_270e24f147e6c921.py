def identifiers(self, identifiers):
    if isinstance(identifiers, subject_abcs.IdentifierCollection
        ) or identifiers is None:
        self._identifiers = identifiers
    else:
        raise ValueError('must use IdentifierCollection')