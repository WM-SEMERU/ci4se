def check_uniqe(self, obj_class, error_msg=_('Must be unique'), **kwargs):
    if obj_class.objects.filter(**kwargs).exclude(pk=self.instance.pk):
        raise forms.ValidationError(error_msg)