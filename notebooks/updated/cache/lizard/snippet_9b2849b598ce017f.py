def _parse_impact_header(hdr_dict):
    desc = hdr_dict['Description']
    if hdr_dict['ID'] == 'ANN':
        parts = [x.strip('"\'') for x in re.split('\\s*\\|\\s*', desc.split
            (':', 1)[1].strip('" '))]
    elif hdr_dict['ID'] == 'EFF':
        parts = [x.strip(' [])\'("') for x in re.split('\\||\\(', desc.
            split(':', 1)[1].strip())]
    elif hdr_dict['ID'] == 'CSQ':
        parts = [x.strip(' [])\'("') for x in re.split('\\||\\(', desc.
            split(':', 1)[1].strip())]
    elif hdr_dict['ID'] == 'BCSQ':
        parts = desc.split(']', 1)[1].split(']')[0].replace('[', '').split('|')
    else:
        raise Exception("don't know how to use %s as annotation" % hdr_dict
            ['ID'])
    return parts