def identification_field_factory(label, error_required):
    return forms.CharField(label=label, widget=forms.TextInput(attrs=
        attrs_dict), max_length=75, error_messages={'required': error_required}
        )