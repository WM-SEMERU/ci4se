def _is_a_url(input_element):
    if type(input_element) is str:
        if any(mark in input_element for mark in ['http://', 'https://',
            'www.', '.pt', '.com', '.org', '.net']):
            return True
        else:
            return False
    else:
        return False