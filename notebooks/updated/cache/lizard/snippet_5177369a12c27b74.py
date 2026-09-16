def actors(self):
    result = []
    actors = self._safe_get_element('ItemAttributes.Actor') or []
    for actor in actors:
        result.append(actor.text)
    return result