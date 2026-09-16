def _check_load_parameters(self, **kwargs):
    if 'partition' in kwargs:
        msg = (
            "'partition' is not allowed as a load parameter. Vcmp guests are accessed by name."
            )
        raise DisallowedReadParameter(msg)
    super(Virtual_Disk, self)._check_load_parameters(**kwargs)