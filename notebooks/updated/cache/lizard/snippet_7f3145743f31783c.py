def get_biopython_pepstats(self, clean_seq=False):
    if self.seq:
        if clean_seq:
            seq = self.seq_str.replace('X', '').replace('U', '')
        else:
            seq = self.seq_str
        try:
            pepstats = (ssbio.protein.sequence.properties.residues.
                biopython_protein_analysis(seq))
        except KeyError as e:
            log.error(
                '{}: unable to run ProteinAnalysis module, unknown amino acid {}'
                .format(self.id, e))
            return
        except ValueError as e:
            log.error('{}: unable to run ProteinAnalysis module, {}'.format
                (self.id, e))
            return
        self.annotations.update(pepstats)
    else:
        raise ValueError(
            '{}: no sequence available, unable to run ProteinAnalysis'.
            format(self.id))