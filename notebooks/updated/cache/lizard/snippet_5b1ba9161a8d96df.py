def _get_translation_field_names():
    from .models import Translation
    fields = [f.name for f in Translation._meta.get_fields()]
    fields.remove('id')
    return fields