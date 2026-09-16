def snip_line(line, max_width, split_at):
    if len(line) < max_width:
        return line
    return line[:split_at] + ' … ' + line[-(max_width - split_at - 3):]