def pad_batch(batch, max_len=0, type='int'):
    batch_size = len(batch)
    max_sent_len = int(np.max([len(x) for x in batch]))
    if max_len > 0 and max_len < max_sent_len:
        max_sent_len = max_len
    if type == 'float':
        idx_matrix = np.zeros((batch_size, max_sent_len), dtype=np.float32)
    else:
        idx_matrix = np.zeros((batch_size, max_sent_len), dtype=np.int)
    for idx1, i in enumerate(batch):
        for idx2, j in enumerate(i):
            if idx2 >= max_sent_len:
                break
            idx_matrix[idx1, idx2] = j
    idx_matrix = torch.tensor(idx_matrix)
    mask_matrix = torch.tensor(torch.eq(idx_matrix.data, 0))
    return idx_matrix, mask_matrix