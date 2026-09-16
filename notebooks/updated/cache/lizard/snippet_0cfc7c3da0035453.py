def find_rmlst_type(kma_report, rmlst_report):
    genes_to_use = dict()
    score_dict = dict()
    gene_alleles = list()
    with open(kma_report) as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter='\t')
        for row in reader:
            gene_allele = row['#Template']
            score = int(row['Score'])
            gene = gene_allele.split('_')[0]
            allele = gene_allele.split('_')[1]
            if gene not in score_dict:
                score_dict[gene] = score
                genes_to_use[gene] = allele
            elif score > score_dict[gene]:
                score_dict[gene] = score
                genes_to_use[gene] = allele
    for gene in genes_to_use:
        gene_alleles.append(gene + '_' + genes_to_use[gene].replace(' ', ''))
    gene_alleles = sorted(gene_alleles)
    with open(rmlst_report, 'w') as f:
        f.write('Gene,Allele\n')
        for gene_allele in gene_alleles:
            gene = gene_allele.split('_')[0]
            allele = gene_allele.split('_')[1]
            f.write('{},{}\n'.format(gene, allele))
    return gene_alleles