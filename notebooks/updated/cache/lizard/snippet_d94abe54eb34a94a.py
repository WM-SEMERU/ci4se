def from_str(string):
    match = re.match('^FINISH READING (\\w+)$', string)
    if match:
        return SetFinishedEvent(match.group(1))
    else:
        raise EventParseError