def check(self, topic, value):
    datatype_key = topic.meta.get('datatype', 'none')
    self._datatypes[datatype_key].check(topic, value)
    validate_dt = topic.meta.get('validate', None)
    if validate_dt:
        self._datatypes[validate_dt].check(topic, value)