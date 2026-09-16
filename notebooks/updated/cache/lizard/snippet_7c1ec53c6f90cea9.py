def ref2names2commdct(ref2names, commdct):
    for comm in commdct:
        for cdct in comm:
            try:
                refs = cdct['object-list'][0]
                validobjects = ref2names[refs]
                cdct.update({'validobjects': validobjects})
            except KeyError as e:
                continue
    return commdct