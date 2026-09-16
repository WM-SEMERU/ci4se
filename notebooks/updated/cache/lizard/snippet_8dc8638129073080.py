def fixChromName(name, orgn='medicago'):
    import re
    mtr_pat1 = re.compile('Mt[0-9]+\\.[0-9]+[\\.[0-9]+]{0,}_([a-z]+[0-9]+)')
    mtr_pat2 = re.compile('([A-z0-9]+)_[A-z]+_[A-z]+')
    zmays_pat = re.compile('[a-z]+:[A-z0-9]+:([A-z0-9]+):[0-9]+:[0-9]+:[0-9]+')
    zmays_sub = {'mitochondrion': 'Mt', 'chloroplast': 'Pt'}
    if orgn == 'medicago':
        for mtr_pat in (mtr_pat1, mtr_pat2):
            match = re.search(mtr_pat, name)
            if match:
                n = match.group(1)
                n = n.replace('0', '')
                name = re.sub(mtr_pat, n, name)
    elif orgn == 'maize':
        match = re.search(zmays_pat, name)
        if match:
            n = match.group(1)
            name = re.sub(zmays_pat, n, name)
            if name in zmays_sub:
                name = zmays_sub[name]
    return name