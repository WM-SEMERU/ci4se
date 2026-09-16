def _j9SaveCurrent(sDir='.'):
    dname = os.path.normpath(sDir + '/' + datetime.datetime.now().strftime(
        '%Y-%m-%d_J9_AbbreviationDocs'))
    if not os.path.isdir(dname):
        os.mkdir(dname)
        os.chdir(dname)
    else:
        os.chdir(dname)
    for urlID, urlString in j9urlGenerator(nameDict=True).items():
        fname = '{}_abrvjt.html'.format(urlID)
        f = open(fname, 'wb')
        f.write(urllib.request.urlopen(urlString).read())