def filter_content_types(self, content_type_qs):
    valid_ct_ids = []
    for ct in content_type_qs:
        model = ct.model_class()
        if model and issubclass(model, EventBase):
            valid_ct_ids.append(ct.id)
    return content_type_qs.filter(pk__in=valid_ct_ids)