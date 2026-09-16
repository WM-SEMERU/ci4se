def summarizeReads(file_handle, file_type):
    base_counts = defaultdict(int)
    read_number = 0
    total_length = 0
    length_list = []
    records = SeqIO.parse(file_handle, file_type)
    for record in records:
        total_length += len(record)
        read_number += 1
        length_list.append(len(record))
        for base in record:
            base_counts[base] += 1
    result = {'read_number': read_number, 'total_length': total_length,
        'average_length': total_length / read_number if read_number > 0 else
        0, 'max_length': max(length_list) if length_list else 0,
        'min_length': min(length_list) if length_list else 0,
        'median_length': median(length_list) if length_list else 0,
        'base_counts': base_counts}
    return result