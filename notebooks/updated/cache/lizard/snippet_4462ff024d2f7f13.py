def parse_kegg_gene_metadata(infile):
    metadata = defaultdict(str)
    with open(infile) as mf:
        kegg_parsed = bs_kegg.parse(mf.read())
    if 'DBLINKS' in kegg_parsed.keys():
        if 'UniProt' in kegg_parsed['DBLINKS']:
            unis = str(kegg_parsed['DBLINKS']['UniProt']).split(' ')
            if isinstance(unis, list):
                metadata['uniprot'] = unis[0]
            else:
                metadata['uniprot'] = unis
        if 'NCBI-ProteinID' in kegg_parsed['DBLINKS']:
            metadata['refseq'] = str(kegg_parsed['DBLINKS']['NCBI-ProteinID'])
    if 'STRUCTURE' in kegg_parsed.keys():
        metadata['pdbs'] = str(kegg_parsed['STRUCTURE']['PDB']).split(' ')
    else:
        metadata['pdbs'] = None
    if 'ORGANISM' in kegg_parsed.keys():
        metadata['taxonomy'] = str(kegg_parsed['ORGANISM'])
    return metadata