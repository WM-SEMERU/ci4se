def _get_css_class(self, ttype):
    ttypeclass = _get_ttype_class(ttype)
    if ttypeclass:
        return self.classprefix + ttypeclass
    return ''