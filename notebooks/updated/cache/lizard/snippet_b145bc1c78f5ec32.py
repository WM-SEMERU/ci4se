def save_existing(self, form, instance, commit=True):
    self._prepare_multilingual_object(instance, form)
    return forms.save_instance(form, instance, exclude=[self._pk_field.name
        ], commit=commit)