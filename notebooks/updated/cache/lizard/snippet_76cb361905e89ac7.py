def parse_string(self):
    if self._parse_string is None:
        parse_text = self._element.xpath('parse/text()')
        if len(parse_text) > 0:
            self._parse_string = parse_text[0]
    return self._parse_string