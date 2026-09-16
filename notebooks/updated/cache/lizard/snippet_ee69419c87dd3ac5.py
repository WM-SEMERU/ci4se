def handle_matches(self, match):
    response = Statement(text='')
    from_parsed = match.group('from')
    target_parsed = match.group('target')
    n_statement = match.group('number')
    if n_statement == 'a' or n_statement == 'an':
        n_statement = '1.0'
    n = mathparse.parse(n_statement, self.language.ISO_639.upper())
    ureg = UnitRegistry()
    from_parsed, target_parsed = self.get_valid_units(ureg, from_parsed,
        target_parsed)
    if from_parsed is None or target_parsed is None:
        response.confidence = 0.0
    else:
        from_value = ureg.Quantity(float(n), from_parsed)
        target_value = from_value.to(target_parsed)
        response.confidence = 1.0
        response.text = str(target_value.magnitude)
    return response