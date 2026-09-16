def _sort_by_unique_fields(model, model_objs, unique_fields):
    unique_fields = [field for field in model._meta.fields if field.attname in
        unique_fields]

    def sort_key(model_obj):
        return tuple(field.get_db_prep_save(getattr(model_obj, field.
            attname), connection) for field in unique_fields)
    return sorted(model_objs, key=sort_key)