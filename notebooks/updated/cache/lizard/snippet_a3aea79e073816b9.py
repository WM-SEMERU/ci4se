def get_residue_mapping(self):
    if len(self.sequence_ids) == 2:
        if not self.alignment_output:
            self.align()
        assert self.alignment_output
        return self._create_residue_map(self._get_alignment_lines(), self.
            sequence_ids[1], self.sequence_ids[2])
    else:
        return None