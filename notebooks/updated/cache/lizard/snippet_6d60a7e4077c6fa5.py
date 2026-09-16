def pfxdtag(tag):
    uri, tagroot = tag[1:].split('}')
    prefix = reverse_nsmap[uri]
    return '%s:%s' % (prefix, tagroot)