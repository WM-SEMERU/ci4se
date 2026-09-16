def potcar_eatom_list_from_outcar(filename='OUTCAR'):
    with open(filename) as f:
        outcar = f.read()
    eatom_re = re.compile('energy of atom\\s+\\d+\\s+EATOM=\\s*([-\\d\\.]+)')
    eatom = [float(e) for e in eatom_re.findall(outcar)]
    return eatom