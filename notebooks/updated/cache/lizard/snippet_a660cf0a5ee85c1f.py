def formatted_param_type(ptype):
    pt_name = ptype['name']
    if pt_name.startswith('<byname>'):
        pt_name = pt_name.replace('<byname>[', '=> ')[:-1]
    elif pt_name.startswith('<repeated>'):
        pt_name = pt_name.replace('<repeated>[', '')[:-1] + '*'
    return pt_name