def get_coordination_numbers(d):
    structure = Structure.from_dict(d['output']['crystal'])
    f = VoronoiNN()
    cn = []
    for i, s in enumerate(structure.sites):
        try:
            n = f.get_cn(structure, i)
            number = int(round(n))
            cn.append({'site': s.as_dict(), 'coordination': number})
        except Exception:
            logger.error('Unable to parse coordination errors')
    return cn