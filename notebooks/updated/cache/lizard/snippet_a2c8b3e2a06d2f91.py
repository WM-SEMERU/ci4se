def _raise_on_bad_representation(representation):
    if representation not in REPRESENTATIONS:
        repr_desc = ', '.join(map(repr, REPRESENTATIONS))
        raise ValueError('Unknown representation: %r (should be one of %s)' %
            (representation, repr_desc))