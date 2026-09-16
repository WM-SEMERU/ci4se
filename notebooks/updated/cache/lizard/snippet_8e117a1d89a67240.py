def list_group_participants(self, appointment_group, **kwargs):
    warnings.warn(
        '`list_group_participants` is being deprecated and will be removed in a future version. Use `get_group_participants` instead'
        , DeprecationWarning)
    return self.get_group_participants(appointment_group, **kwargs)