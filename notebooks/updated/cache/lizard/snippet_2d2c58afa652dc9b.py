def index(self, overwrite=False):
    if self.requires_gtf:
        self.db.connect_or_create(overwrite=overwrite)
    if self.requires_transcript_fasta:
        self.transcript_sequences.index(overwrite=overwrite)
    if self.requires_protein_fasta:
        self.protein_sequences.index(overwrite=overwrite)