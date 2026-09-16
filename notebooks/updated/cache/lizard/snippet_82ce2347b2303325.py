def get_color(self, refresh=False):
    if refresh:
        self.refresh_complex_value('CurrentColor')
    ci = self.get_color_index(['R', 'G', 'B'], refresh)
    cur = self.get_complex_value('CurrentColor')
    if ci is None or cur is None:
        return None
    try:
        val = [cur.split(',')[c] for c in ci]
        return [int(v.split('=')[1]) for v in val]
    except IndexError:
        return None