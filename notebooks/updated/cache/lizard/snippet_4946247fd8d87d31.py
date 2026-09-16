def get_bank_form(self, *args, **kwargs):
    if isinstance(args[-1], list) or 'bank_record_types' in kwargs:
        return self.get_bank_form_for_create(*args, **kwargs)
    else:
        return self.get_bank_form_for_update(*args, **kwargs)