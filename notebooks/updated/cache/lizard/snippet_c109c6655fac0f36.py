def setup_allelespecific_database(fasta_file, database_folder, allele_list):
    index = SeqIO.index(os.path.join(database_folder,
        'rMLST_combined.fasta'), 'fasta')
    seqs = list()
    for s in allele_list:
        try:
            seqs.append(index[s])
        except KeyError:
            logging.warning(
                'Tried to add {} to allele-specific database, but could not find it.'
                .format(s))
    SeqIO.write(seqs, fasta_file, 'fasta')