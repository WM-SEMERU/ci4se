def positions_to_contigs(positions):
    contig_labels = np.zeros_like(positions)
    contig_index = 0
    for i, p in enumerate(positions):
        if p == 0:
            contig_index += 1
        contig_labels[i] = contig_index
    return contig_labels