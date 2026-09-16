def create_dexseq_annotation(gff, count_file):
    out_file = count_file + '.ann'
    if file_exists(out_file):
        return out_file
    with file_transaction(out_file) as tx_out:
        with open(tx_out, 'w') as out_handle:
            with open(gff) as in_handle:
                for line in in_handle:
                    cols = line.strip().split('\t')
                    if cols[2] == 'exonic_part':
                        exon = [f for f in cols[8].split(';') if f.strip().
                            startswith('exonic_part_number')]
                        gene = [f for f in cols[8].split(';') if f.strip().
                            startswith('gene_id')]
                        exon = exon[0].replace('"', '').split()[1]
                        gene = gene[0].replace('"', '').split()[1]
                        length = int(cols[4]) - int(cols[3]) + 1
                        line = '%s:%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (gene,
                            exon, gene, cols[0], cols[3], cols[4], length,
                            cols[6])
                        out_handle.write(line)