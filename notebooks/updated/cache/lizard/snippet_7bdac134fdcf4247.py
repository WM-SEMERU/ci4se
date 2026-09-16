def get_groups(self, load):
    if 'eauth' not in load:
        return False
    fstr = '{0}.groups'.format(load['eauth'])
    if fstr not in self.auth:
        return False
    fcall = salt.utils.args.format_call(self.auth[fstr], load,
        expected_extra_kws=AUTH_INTERNAL_KEYWORDS)
    try:
        return self.auth[fstr](*fcall['args'], **fcall['kwargs'])
    except IndexError:
        return False
    except Exception:
        return None