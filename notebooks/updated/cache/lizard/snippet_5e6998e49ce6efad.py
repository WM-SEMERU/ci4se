def enforce(self, enforce_bounds='reset'):
    if isinstance(enforce_bounds, bool):
        import warnings
        warnings.warn('deprecation warning: enforce_bounds should be ' +
            "either 'reset', 'drop', 'scale', or None, not bool" +
            '...resetting to None.', PyemuWarning)
        enforce_bounds = None
    if enforce_bounds is None:
        return
    if enforce_bounds.lower() == 'reset':
        self.enforce_reset()
    elif enforce_bounds.lower() == 'drop':
        self.enforce_drop()
    elif enforce_bounds.lower() == 'scale':
        self.enfore_scale()
    else:
        raise Exception('unrecognized enforce_bounds arg:' +
            "{0}, should be 'reset' or 'drop'".format(enforce_bounds))