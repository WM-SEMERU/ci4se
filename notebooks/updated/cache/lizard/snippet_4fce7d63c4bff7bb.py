def sap_sid_nr(broker):
    insts = broker[DefaultSpecs.saphostctrl_listinstances].content
    hn = broker[DefaultSpecs.hostname].content[0].split('.')[0].strip()
    results = set()
    for ins in insts:
        ins_splits = ins.split(' - ')
        if ins_splits[2].strip() == hn:
            results.add((ins_splits[0].split()[-1].lower(), ins_splits[1].
                strip()))
    return list(results)