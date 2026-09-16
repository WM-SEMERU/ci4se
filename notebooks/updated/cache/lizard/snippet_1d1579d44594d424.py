def _download_py2(link, path, __hdr__):
    try:
        req = urllib2.Request(link, headers=__hdr__)
        u = urllib2.urlopen(req)
    except Exception as e:
        raise Exception(' Download failed with the error:\n{}'.format(e))
    with open(path, 'wb') as outf:
        for l in u:
            outf.write(l)
    u.close()