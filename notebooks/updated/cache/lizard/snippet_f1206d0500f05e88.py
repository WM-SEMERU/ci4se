def kmer_count(seq_list, k):
    all_kmers = generate_all_kmers(k)
    kmer_count_list = []
    for seq in seq_list:
        kmer_count_list.append([seq.count(kmer) for kmer in all_kmers])
    return pd.DataFrame(kmer_count_list, columns=all_kmers)