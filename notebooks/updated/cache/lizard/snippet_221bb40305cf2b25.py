def get_variant_id(variant_dict=None, variant_line=None):
    if variant_dict:
        chrom = variant_dict['CHROM']
        position = variant_dict['POS']
        ref = variant_dict['REF']
        alt = variant_dict['ALT']
    elif variant_line:
        splitted_line = variant_line.rstrip().split('\t')
        chrom = splitted_line[0]
        position = splitted_line[1]
        ref = splitted_line[3]
        alt = splitted_line[4]
    else:
        raise Exception('Have to provide variant dict or variant line')
    return '_'.join([chrom, position, ref, alt])