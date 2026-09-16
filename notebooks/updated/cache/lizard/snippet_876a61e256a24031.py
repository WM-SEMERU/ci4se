def validate(self):
    validate_edge_direction(self.direction)
    validate_safe_string(self.edge_name)
    if not isinstance(self.within_optional_scope, bool):
        raise TypeError('Expected bool within_optional_scope, got: {} {}'.
            format(type(self.within_optional_scope).__name__, self.
            within_optional_scope))
    if not isinstance(self.depth, int):
        raise TypeError('Expected int depth, got: {} {}'.format(type(self.
            depth).__name__, self.depth))
    if not self.depth >= 1:
        raise ValueError('depth ({}) >= 1 does not hold!'.format(self.depth))