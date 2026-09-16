def _cache_key_select_daterange(method, self, field_id, field_title, style=None
    ):
    key = update_timer(), field_id, field_title, style
    return key