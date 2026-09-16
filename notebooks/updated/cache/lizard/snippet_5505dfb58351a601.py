def FromString(cls, desc):
    if language.stream is None:
        language.get_language()
    parse_exp = Optional(time_interval('time') - Literal(':').suppress()
        ) - language.stream('stream') - Literal('=').suppress() - number(
        'value')
    try:
        data = parse_exp.parseString(desc)
        time = 0
        if 'time' in data:
            time = data['time'][0]
        return SimulationStimulus(time, data['stream'][0], data['value'])
    except (ParseException, ParseSyntaxException):
        raise ArgumentError('Could not parse stimulus descriptor',
            descriptor=desc)