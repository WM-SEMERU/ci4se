def _details(self, nohtml=False):
    text = ''
    inst = self.timemachine
    if self.action_type in ('dl', 'cr'):
        fields = inst.fields + inst.foreignkeys
    else:
        fields = [i.key for i in self.modification_commits.all()]
    for field in fields:
        if not nohtml:
            text += '<strong>%s</strong>: ' % field
        else:
            text += '%s: ' % field
        if self.action_type == 'md':
            if not nohtml:
                text += ('%s &#8594; ' % inst.at_previous_action.
                    _field_value_html(field))
            else:
                text += '%s -> ' % inst.at_previous_action._field_value_text(
                    field)
        if not nohtml:
            text += '%s<br/>' % inst._field_value_html(field)
        else:
            text += '%s\n' % inst._field_value_text(field)
    return text