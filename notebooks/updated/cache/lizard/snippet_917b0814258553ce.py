def render_choicefield(field, attrs, choices=None):
    if not choices:
        choices = format_html_join('', wrappers.CHOICE_TEMPLATE,
            get_choices(field))
    field.field.widget.attrs['value'] = field.value() or attrs.get('value', '')
    return wrappers.DROPDOWN_WRAPPER % {'name': field.html_name, 'attrs':
        pad(flatatt(field.field.widget.attrs)), 'placeholder': attrs.get(
        'placeholder') or get_placeholder_text(), 'style': pad(attrs.get(
        '_style', '')), 'icon': format_html(wrappers.ICON_TEMPLATE, attrs.
        get('_dropdown_icon') or 'dropdown'), 'choices': choices}