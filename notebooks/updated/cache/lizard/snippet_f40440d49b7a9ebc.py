def datetimeparser(fmt, strict=True):

    def parser(value):
        try:
            return datetime.datetime.strptime(value.strip(), fmt)
        except Exception as e:
            if strict:
                raise e
            else:
                return value
    return parser