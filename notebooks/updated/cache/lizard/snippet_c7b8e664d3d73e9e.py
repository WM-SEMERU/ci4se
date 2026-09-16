def download_seq_file(self, outdir, force_rerun=False):
    uniprot_fasta_file = download_uniprot_file(uniprot_id=self.id, filetype
        ='fasta', outdir=outdir, force_rerun=force_rerun)
    self.sequence_path = uniprot_fasta_file