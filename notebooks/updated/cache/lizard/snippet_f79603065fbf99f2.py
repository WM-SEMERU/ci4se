def home_abbreviation(self):
    abbr = re.sub('.*/teams/', '', str(self._home_name))
    abbr = re.sub('/.*', '', abbr)
    return abbr