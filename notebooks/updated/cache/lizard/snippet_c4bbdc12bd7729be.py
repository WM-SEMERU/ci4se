def _pick_align_split_size(total_size, target_size, target_size_reads,
    max_splits):
    if total_size // target_size > max_splits:
        piece_size = total_size // max_splits
        return int(piece_size * target_size_reads / target_size)
    else:
        return int(target_size_reads)