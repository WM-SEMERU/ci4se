def gather_dilated_memory_blocks(x, num_memory_blocks, gap_size,
    query_block_size, memory_block_size, gather_indices, direction='left'):
    gathered_blocks = []
    for block_id in range(num_memory_blocks):
        block_end_index = -(query_block_size + gap_size * (block_id + 1) + 
            memory_block_size * block_id)
        block_start_index = (memory_block_size + gap_size) * (num_memory_blocks
             - (block_id + 1))
        if direction != 'left':
            [block_end_index, block_start_index] = [-block_start_index, -
                block_end_index]
        if block_end_index == 0:
            x_block = x[block_start_index:]
        else:
            x_block = x[block_start_index:block_end_index]

        def gather_dilated_1d_blocks(x, gather_indices):
            x_new = tf.gather(x, gather_indices)
            return tf.transpose(x_new, [2, 3, 0, 1, 4])
        gathered_blocks.append(gather_dilated_1d_blocks(x_block,
            gather_indices))
    return tf.concat(gathered_blocks, 3)