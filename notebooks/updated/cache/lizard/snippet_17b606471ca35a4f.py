def crispy_addon(field, append='', prepend='', form_show_labels=True):
    if field:
        context = Context({'field': field, 'form_show_errors': True,
            'form_show_labels': form_show_labels})
        template = loader.get_template(
            '%s/layout/prepended_appended_text.html' % get_template_pack())
        context['crispy_prepended_text'] = prepend
        context['crispy_appended_text'] = append
        if not prepend and not append:
            raise TypeError('Expected a prepend and/or append argument')
        context = context.flatten()
    return template.render(context)