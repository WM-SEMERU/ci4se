def get_asset_form(self, *args, **kwargs):
    if isinstance(args[-1], list) or 'asset_record_types' in kwargs:
        return self.get_asset_form_for_create(*args, **kwargs)
    else:
        return self.get_asset_form_for_update(*args, **kwargs)