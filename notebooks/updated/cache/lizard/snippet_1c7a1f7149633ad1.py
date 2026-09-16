def rename_genome(genome_in, genome_out=None):
    if genome_out is None:
        genome_out = '{}_renamed.fa'.format(genome_in.split('.')[0])
    with open(genome_out, 'w') as output_handle:
        for record in SeqIO.parse(genome_in, 'fasta'):
            new_record_id = record.id.replace(' ', '_')
            new_record_id = new_record_id.replace('-', '_')
            new_record_id = new_record_id.replace('\t', '_')
            new_record_id = re.sub('[^_A-Za-z0-9]+', '', new_record_id)
            header = '>{}\n'.format(new_record_id)
            output_handle.write(header)
            output_handle.write('{}\n'.format(str(record.seq)))