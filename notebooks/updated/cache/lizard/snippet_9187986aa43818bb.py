def _trim_xpath(self, xpath, prop):
    xroot = self._get_xroot_for(prop)
    if xroot is None and isinstance(xpath, string_types):
        xtags = xpath.split(XPATH_DELIM)
        if xtags[-1] in _iso_tag_primitives:
            xroot = XPATH_DELIM.join(xtags[:-1])
    return xroot