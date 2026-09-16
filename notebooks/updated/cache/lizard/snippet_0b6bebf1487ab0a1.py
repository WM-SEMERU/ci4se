def parse_headers(cls, msg):
    return list(email.parser.Parser().parsestr(msg).items())