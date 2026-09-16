def render_iconchoicefield(field, attrs):
    choices = ''
    for choice in field.field._choices:
        value = choice[1].split('|')
        choices += format_html(wrappers.ICON_CHOICE_TEMPLATE, choice[0],
            mark_safe(wrappers.ICON_TEMPLATE.format(value[-1])), value[0])
    return render_choicefield(field, attrs, choices)