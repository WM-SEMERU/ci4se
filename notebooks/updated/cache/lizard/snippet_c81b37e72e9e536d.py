def complete(self):
    return (self.contains_start_codon and self.contains_stop_codon and self
        .coding_sequence is not None and len(self.coding_sequence) % 3 == 0)