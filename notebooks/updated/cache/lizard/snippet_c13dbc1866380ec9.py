def _defaults(cls):
    minimum_needs = {'resources': [{'Default': '2.8', 'Minimum allowed':
        '0', 'Maximum allowed': '100', 'Frequency': 'weekly',
        'Resource name': cls.Rice, 'Resource description': 'Basic food',
        'Unit': 'kilogram', 'Units': 'kilograms', 'Unit abbreviation': 'kg',
        'Readable sentence':
        'Each person should be provided with {{ Default }} {{ Units }} of {{ Resource name }} {{ Frequency }}.'
        }, {'Default': '17.5', 'Minimum allowed': '0', 'Maximum allowed':
        '100', 'Frequency': 'weekly', 'Resource name': cls.Drinking_water,
        'Resource description': 'For drinking', 'Unit': 'litre', 'Units':
        'litres', 'Unit abbreviation': 'l', 'Readable sentence':
        'Each person should be provided with {{ Default }} {{ Units }} of {{ Resource name }} {{ Frequency }} for drinking.'
        }, {'Default': '67', 'Minimum allowed': '10', 'Maximum allowed':
        '100', 'Frequency': 'weekly', 'Resource name': cls.Water,
        'Resource description': 'For washing', 'Unit': 'litre', 'Units':
        'litres', 'Unit abbreviation': 'l', 'Readable sentence':
        'Each person should be provided with {{ Default }} {{ Units }} of {{ Resource name }} {{ Frequency }} for washing.'
        }, {'Default': '0.2', 'Minimum allowed': '0.1', 'Maximum allowed':
        '1', 'Frequency': 'weekly', 'Resource name': cls.Family_kits,
        'Resource description': 'Hygiene kits', 'Unit': '', 'Units': '',
        'Unit abbreviation': '', 'Readable sentence':
        'Each family of 5 persons should be provided with 1 Family Kit per week.'
        }, {'Default': '0.05', 'Minimum allowed': '0.02', 'Maximum allowed':
        '1', 'Frequency': 'single', 'Resource name': cls.Toilets,
        'Resource description': '', 'Unit': '', 'Units': '',
        'Unit abbreviation': '', 'Readable sentence':
        'A Toilet should be provided for every 20 persons.'}], 'provenance':
        'The minimum needs are based on Perka 7/2008.', 'profile': 'BNPB_en'}
    return minimum_needs