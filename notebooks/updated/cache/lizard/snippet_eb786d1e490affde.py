def convert_lines_to_block(lines, block_map, link_stack, source_path,
    block_name=ALL_BLOCK_NAME):
    found_closing_block = False
    segments = []
    while lines:
        line = lines.pop(0)
        close_tag_match = BLOCK_CLOSE_REGEX.match(line)
        if close_tag_match:
            if close_tag_match.group(1) != block_name:
                raise InvalidBlockName('Expected closing block ' +
                    block_name + 'but found block named "' +
                    block_tag_match.group(1) + '" in ' + source_path)
            found_closing_block = True
            break
        open_tag_match = BLOCK_OPEN_REGEX.match(line)
        if open_tag_match:
            inner_block_name = open_tag_match.group(1)
            if inner_block_name == ALL_BLOCK_NAME:
                raise InvalidBlockName(
                    '"{0}" is a reserved block name, but found block named "{0}" in {1}'
                    .format(ALL_BLOCK_NAME, source_path))
            inner_block = convert_lines_to_block(lines, block_map,
                link_stack, source_path, inner_block_name)
            segments.append(inner_block)
            continue
        variable_match = VARIABLE_REGEX.match(line)
        if variable_match:
            process_variable(variable_match, block_map)
            continue
        include_match = INCLUDE_REGEX.match(line)
        if include_match:
            included_content = process_links(include_match, block_map,
                link_stack, source_path)
            if included_content != '':
                append_text_to_segments(segments, included_content)
        else:
            append_text_to_segments(segments, line)
    if block_name != ALL_BLOCK_NAME and not found_closing_block:
        raise InvalidBlockName('Expected closing block called "{0}" in {1}'
            .format(block_name, source_path))
    block = Block(source_path, block_name, segments)
    block_map.add_block(block)
    return block