def print_pixy_blocks(blocks):
    print('Detected ' + str(len(blocks)) + ' Pixy blocks:')
    if len(blocks) > 0 and not 'signature' in blocks[0]:
        print(
            'Something went wrong.  This does not appear to be a printable block.'
            )
        board.shutdown()
        return
    for block_index in range(len(blocks)):
        block = blocks[block_index]
        print('  block {}: sig: {}  x: {} y: {} width: {} height: {}'.
            format(block_index, block['signature'], block['x'], block['y'],
            block['width'], block['height']))