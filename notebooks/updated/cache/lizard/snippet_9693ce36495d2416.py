def url_escape(value, plus=True):
    quote = urllib_parse.quote_plus if plus else urllib_parse.quote
    return quote(utf8(value))