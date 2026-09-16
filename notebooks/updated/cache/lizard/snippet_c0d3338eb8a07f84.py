def _return_fieldset(self, fieldset):
    collapsible = None
    description = None
    try:
        int(str(fieldset))
        title = None
    except ValueError:
        if fieldset.count('|') > 1:
            raise ImproperlyConfigured(
                "The fieldset name does not support more than one | sign. It's meant to separate a fieldset from its description."
                )
        title = fieldset
        if '|' in fieldset:
            title, description = fieldset.split('|')
        if fieldset and fieldset[0] in '-+':
            if fieldset[0] == '-':
                collapsible = 'closed'
            else:
                collapsible = 'open'
            title = title[1:]
    return {'title': title, 'description': description, 'collapsible':
        collapsible}