def assemble_caption(begin_line, begin_index, end_line, end_index, lines):
    label_head = '\\label{'
    if end_line > begin_line:
        caption = lines[begin_line][begin_index:]
        for included_line_index in range(begin_line + 1, end_line):
            caption = caption + ' ' + lines[included_line_index]
        caption = caption + ' ' + lines[end_line][:end_index]
        caption = caption.replace('\n', ' ')
        caption = caption.replace('  ', ' ')
    else:
        caption = lines[begin_line][begin_index:end_index]
    label_begin = caption.find(label_head)
    if label_begin > -1:
        dummy_start, dummy_start_line, label_end, dummy_end = (
            find_open_and_close_braces(0, label_begin, '{', [caption]))
        caption = caption[:label_begin] + caption[label_end + 1:]
    caption = caption.strip()
    if len(caption) > 1 and caption[0] == '{' and caption[-1] == '}':
        caption = caption[1:-1]
    return caption