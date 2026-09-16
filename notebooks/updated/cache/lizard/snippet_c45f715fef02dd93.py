def replace_token(self, sid, sinfo, token_type):
    try:
        refresh_token = self.handler[token_type](sid, sinfo=sinfo)
    except KeyError:
        pass
    else:
        try:
            self.handler[token_type].black_list(sinfo[token_type])
        except KeyError:
            pass
        sinfo[token_type] = refresh_token
    return sinfo