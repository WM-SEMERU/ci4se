def get_block_dict(top_level_block):
    block_stack = [top_level_block]
    block_dict = {}
    while block_stack:
        block = block_stack.pop()
        block_dict[block.name] = str(block)
        for segment in block.segments:
            if isinstance(segment, Block):
                block_stack.append(segment)
    return block_dict