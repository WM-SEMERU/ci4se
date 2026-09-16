def get_param_text(self, nid):
    r = []
    params = self.parameters.xpath('.//param[@ref-id="{}"]'.format(nid))
    if not params:
        return r
    for param in params:
        vnode = param.find('value')
        s = 'Parameter: {}, type:{}, value: {}'.format(param.attrib.get(
            'name'), vnode.attrib.get('type'), param.findtext('value',
            default='No Value'))
        r.append(s)
    return r