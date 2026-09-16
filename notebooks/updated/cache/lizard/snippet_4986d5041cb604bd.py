def process_form(self, instance, field, form, empty_marker=None,
    emptyReturnsMarker=False):
    if field.getName() != 'ReflexRules':
        return RecordsWidget.process_form(self, instance, field, form,
            empty_marker, emptyReturnsMarker)
    raw_data = RecordsWidget.process_form(self, instance, field, form,
        empty_marker, emptyReturnsMarker)
    value = []
    rulenum = 0
    for raw_set in raw_data[0]:
        d = self._format_conditions_and_actions(raw_set)
        d['rulenumber'] = str(rulenum)
        d['mother_service_uid'] = raw_data[0][0].get('analysisservice-0', '')
        value.append(d)
        rulenum += 1
    return value, {}