def find(self, item, description='', event_type=''):
    if ': ' in item:
        splited = item.split(': ', 1)
        if splited[0] in self.TYPES:
            description = item.split(': ')[1]
            event_type = item.split(': ')[0]
        else:
            description = item
    elif not description:
        description = item
    if event_type:
        found = [x['time'] for x in self.log if re.search(description, x[
            'description']) and x['eventTypeText'] == event_type]
    else:
        found = [x['time'] for x in self.log if re.search(description, x[
            'description'])]
    if len(found):
        return found
    raise exceptions.NotFoundError(
        "Item '{}' is not found with (description='{}', event_type='{}')".
        format(item, description, event_type))