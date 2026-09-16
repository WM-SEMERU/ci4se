def errors(self, instance):
    if isinstance(instance, dict):
        return self._validate(instance)
    elif isinstance(instance, forms.BaseForm):
        if instance.is_bound and instance.is_valid():
            return self._validate(instance.cleaned_data)
        return self._validate(dict([(f, instance.initial.get(f, instance[f]
            .value())) for f in self.validators]))
    elif isinstance(instance, formsets.BaseFormSet):
        if instance.can_delete:
            validate_forms = [form for form in instance.initial_forms if 
                not instance._should_delete_form(form)] + [form for form in
                instance.extra_forms if form.has_changed() and not instance
                ._should_delete_form(form)]
            return [self.errors(f) for f in validate_forms]
        else:
            validate_forms = instance.initial_forms + [form for form in
                instance.extra_forms if form.has_changed()]
            return [self.errors(f) for f in validate_forms]
    elif isinstance(instance, models.Model):
        return self._validate(dict([(f, getattr(instance, f)) for f in self
            .validators]))