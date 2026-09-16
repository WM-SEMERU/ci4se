def download(url, localFileName=None, localDirName=None):
    localName = url2name(url)
    req = Request(url)
    r = urlopen(req)
    if r.info().has_key('Content-Disposition'):
        localName = r.info()['Content-Disposition'].split('filename=')
        if len(localName) > 1:
            localName = localName[1]
            if localName[0] == '"' or localName[0] == "'":
                localName = localName[1:-1]
        else:
            localName = url2name(r.url)
    elif r.url != url:
        localName = url2name(r.url)
    if localFileName:
        localName = localFileName
    if localDirName:
        if not os.path.exists(localDirName):
            os.makedirs(localDirName)
        localName = os.path.join(localDirName, localName)
    f = open(localName, 'wb')
    f.write(r.read())
    f.close()