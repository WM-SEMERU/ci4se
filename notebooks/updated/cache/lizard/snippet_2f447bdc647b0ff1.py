def res_set_to_phenotype(res_set, full_list):
    full_list = list(full_list)
    phenotype = len(full_list) * ['0']
    for i in range(len(full_list)):
        if full_list[i] in res_set:
            phenotype[i] = '1'
    assert phenotype.count('1') == len(res_set)
    while phenotype[0] == '0' and len(phenotype) > 1:
        phenotype = phenotype[1:]
    return '0b' + ''.join(phenotype)