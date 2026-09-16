def clean_translation(self):
    translation = self.cleaned_data['translation']
    if self.instance and self.instance.content_object:
        obj = self.instance.content_object
        field = obj._meta.get_field(self.instance.field)
        max_length = field.max_length
        if max_length and len(translation) > max_length:
            raise forms.ValidationError(_(
                'The entered translation is too long. You entered %(entered)s chars, max length is %(maxlength)s'
                ) % {'entered': len(translation), 'maxlength': max_length})
    else:
        raise forms.ValidationError(_(
            'Can not store translation. First create all translation for this object'
            ))
    return translation