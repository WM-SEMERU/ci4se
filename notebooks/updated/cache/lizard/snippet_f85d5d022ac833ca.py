def _page_text(page, nowrap=False):
    title = page.data['title']
    title = '%s\n%s' % (title, '=' * len(title))
    desc = page.data.get('description')
    if desc:
        desc = '_%s_' % desc
    img = _text_image(page)
    pars = page.data.get('extext')
    if pars:
        pars = re.sub('[ ]+\\*[ ]+', '* ', pars)
    if pars and not nowrap:
        parlist = []
        for par in pars.split('\n\n'):
            parlist.append('\n'.join(textwrap.wrap(par)))
        disambiguation = page.data.get('disambiguation')
        if disambiguation:
            parlist.append(' * ' + '\n * '.join(page.data.get('links')))
        pars = '\n\n'.join(parlist)
    url = '<%s>' % page.data['url']
    txt = []
    txt.append(title)
    txt.append(desc)
    txt.append(url)
    txt.append(pars)
    txt.append(img)
    return '\n\n'.join([x for x in txt if x])