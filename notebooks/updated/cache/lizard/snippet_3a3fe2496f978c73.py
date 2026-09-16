def server_link(rel, server_id=None, self_rel=False):
    servers_href = '/v1/servers'
    link = _SERVER_LINKS[rel].copy()
    link['href'] = link['href'].format(**locals())
    link['rel'] = 'self' if self_rel else rel
    return link