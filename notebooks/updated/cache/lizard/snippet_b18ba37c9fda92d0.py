def VR(VR=None, description=None):
    value_repr = {'AE': 'Application Entity', 'AS': 'Age String', 'AT':
        'Attribute Tag', 'CS': 'Code String', 'DA': 'Date', 'DS':
        'Decimal String', 'DT': 'Date/Time', 'FL':
        'Floating Point Single (4 bytes)', 'FD':
        'Floating Point Double (8 bytes)', 'IS': 'Integer String', 'LO':
        'Long String', 'LT': 'Long Text', 'OB': 'Other Byte', 'OF':
        'Other Float', 'OW': 'Other Word', 'PN': 'Person Name', 'SH':
        'Short String', 'SL': 'Signed Long', 'SQ': 'Sequence of Items',
        'SS': 'Signed Short', 'ST': 'Short Text', 'TM': 'Time', 'UI':
        'Unique Identifier', 'UL': 'Unsigned Long', 'UN': 'Unknown', 'US':
        'Unsigned Short', 'UT': 'Unlimited Text'}
    assert VR or description, 'Either VR or description required to map VR'
    if VR is not None:
        VR = VR.upper()
        if VR in value_repr:
            return value_repr[VR]
    for key, value in value_repr.iteritems():
        if description == value:
            return key
    return None