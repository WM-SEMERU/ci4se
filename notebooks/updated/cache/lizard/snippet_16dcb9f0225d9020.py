def get_line_bad_footnotes(line, tag=None, include_tags=None):
    if tag is None or include_tags is None or tag in include_tags or any(
        tag.startswith(t) for t in include_tags):
        found_baddies = re_bad_footnotes.findall(line)
        return [line] + [baddie[0] for baddie in found_baddies]
    return [line]