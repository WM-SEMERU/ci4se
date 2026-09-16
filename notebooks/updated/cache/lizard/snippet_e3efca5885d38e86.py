def sanitize_parse_mode(mode):
    if not mode:
        return None
    if callable(mode):


        class CustomMode:

            @staticmethod
            def unparse(text, entities):
                raise NotImplementedError
        CustomMode.parse = mode
        return CustomMode
    elif all(hasattr(mode, x) for x in ('parse', 'unparse')) and all(
        callable(x) for x in (mode.parse, mode.unparse)):
        return mode
    elif isinstance(mode, str):
        try:
            return {'md': markdown, 'markdown': markdown, 'htm': html,
                'html': html}[mode.lower()]
        except KeyError:
            raise ValueError('Unknown parse mode {}'.format(mode))
    else:
        raise TypeError('Invalid parse mode type {}'.format(mode))