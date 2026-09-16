def get_locus(sequences, kir=False, verbose=False, refdata=None, evalue=10):
    if not refdata:
        refdata = ReferenceData()
    file_id = str(randomid())
    input_fasta = file_id + '.fasta'
    output_xml = file_id + '.xml'
    SeqIO.write(sequences, input_fasta, 'fasta')
    blastn_cline = NcbiblastnCommandline(query=input_fasta, db=refdata.
        blastdb, evalue=evalue, outfmt=5, reward=1, penalty=-3, gapopen=5,
        gapextend=2, dust='yes', out=output_xml)
    stdout, stderr = blastn_cline()
    blast_qresult = SearchIO.read(output_xml, 'blast-xml')
    cleanup(file_id)
    if len(blast_qresult.hits) == 0:
        return ''
    loci = []
    for i in range(0, 3):
        if kir:
            loci.append(blast_qresult[i].id.split('*')[0])
        else:
            loci.append(blast_qresult[i].id.split('*')[0])
    locus = set(loci)
    if len(locus) == 1:
        if has_hla(loci[0]) or kir:
            return loci[0]
        else:
            return 'HLA-' + loci[0]
    else:
        return ''