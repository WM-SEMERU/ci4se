def remove_sequences(self, tree, sequence_names):
    tree.prune_taxa_with_labels(sequence_names)
    tree.prune_taxa_with_labels([s.replace('_', ' ') for s in sequence_names])