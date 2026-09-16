def _parse(self):
    responses = []
    for child in self._element:
        weight = int_attribute(child, 'weight', 1)
        self._log.debug('Parsing random entry with weight {weight}: {entry}'
            .format(weight=weight, entry=child.text))
        if not len(child):
            responses.append((child.text, weight))
            continue
        responses.append((tuple(self.trigger.agentml.parse_tags(child, self
            .trigger)), weight))
    self._responses = tuple(responses)