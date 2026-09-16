def get_kws(self):
    ret = self.kws['dict'].copy()
    act_set = self.kws['set']
    if 'shorten' in act_set and 'goobj2fncname' not in ret:
        ret['goobj2fncname'] = ShortenText().get_short_plot_name
    return ret