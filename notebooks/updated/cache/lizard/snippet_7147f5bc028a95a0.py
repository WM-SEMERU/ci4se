def merge(cls, source_blocks):
    if len(source_blocks) == 1:
        return source_blocks[0]
    source_blocks.sort(key=operator.attrgetter('start_line_number'))
    main_block = source_blocks[0]
    boot_lines = main_block.boot_lines
    source_lines = [source_line for source_block in source_blocks for
        source_line in source_block.source_lines]
    return cls(boot_lines, source_lines, directive=main_block.directive,
        language=main_block.language, roles=main_block.roles)