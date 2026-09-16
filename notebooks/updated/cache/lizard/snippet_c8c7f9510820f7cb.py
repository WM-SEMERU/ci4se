def getPackages(plist):
    nlist = plist.split('\n')
    pkgs = []
    for i in nlist:
        if i.find('===') > 0:
            continue
        pkg = i.split()[0]
        if pkg == 'Warning:':
            continue
        elif pkg == 'Could':
            continue
        elif pkg == 'Some':
            continue
        elif pkg == 'You':
            continue
        elif not pkg:
            continue
        pkgs.append(pkg)
    print('  >> Found', len(pkgs), 'packages')
    return pkgs