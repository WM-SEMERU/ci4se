def render_countryfield(field, attrs):
    choices = ((k, k.lower(), v) for k, v in field.field._choices[1:])
    return render_choicefield(field, attrs, format_html_join('', wrappers.
        COUNTRY_TEMPLATE, choices))