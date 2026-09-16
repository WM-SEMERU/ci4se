def geo_description(self):
    sc = self._p.space_coverage
    gc = self._p.grain_coverage
    if sc and gc:
        if parse_to_gvid(gc[0]).level == 'state' and parse_to_gvid(sc[0]
            ).level == 'state':
            return parse_to_gvid(sc[0]).geo_name
        else:
            return '{} in {}'.format(parse_to_gvid(gc[0]).level_plural.
                title(), parse_to_gvid(sc[0]).geo_name)
    elif sc:
        return parse_to_gvid(sc[0]).geo_name.title()
    elif sc:
        return parse_to_gvid(gc[0]).level_plural.title()
    else:
        return ''