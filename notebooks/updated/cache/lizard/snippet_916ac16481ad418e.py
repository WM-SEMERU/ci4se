def _process_consensus_mhcii(mhc_file, normal=False):
    core_col = None
    results = pandas.DataFrame(columns=['allele', 'pept', 'tumor_pred', 'core']
        )
    with open(mhc_file, 'r') as mf:
        peptides = set()
        for line in mf:
            if not line.startswith('HLA'):
                continue
            line = line.strip().split('\t')
            allele = line[0]
            pept = line[4]
            pred = line[6]
            if core_col:
                core = line[core_col]
            else:
                methods = line[5].lstrip('Consensus(').rstrip(')')
                methods = methods.split(',')
                if 'NN' in methods:
                    core_col = 13
                elif 'netMHCIIpan' in methods:
                    core_col = 17
                elif 'Sturniolo' in methods:
                    core_col = 19
                elif 'SMM' in methods:
                    core_col = 10
                core = line[core_col] if core_col else 'NOCORE'
            if float(pred) > 5.0 and not normal:
                continue
            results.loc[len(results)] = [allele, pept, pred, core]
    results.drop_duplicates(inplace=True)
    return results