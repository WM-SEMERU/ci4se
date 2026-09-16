def action_fields(self):
    url = self.action
    if url is None:
        return {}
    halves = url.split('?')
    if len(halves) == 1:
        return {}
    key_value_pairs = halves[1].split('&')
    return dict([pair.split('=') for pair in key_value_pairs])