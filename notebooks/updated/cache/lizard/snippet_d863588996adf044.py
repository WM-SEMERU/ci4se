def from_str(string):
    match = re.match('^UPDATE (.+)$', string)
    if match:
        parsed_date = dateutil.parser.parse(match.group(1), ignoretz=True)
        return UpdateEvent(parsed_date)
    else:
        raise EventParseError