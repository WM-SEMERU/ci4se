def safe_tag(self, tag, errors='strict'):
    if tag is not None:
        try:
            tag = quote(self.s(tag, errors=errors), safe='~')[:128]
        except KeyError as e:
            warn = 'Failed converting tag to safetag ({})'.format(e)
            self.log.warning(warn)
    return tag