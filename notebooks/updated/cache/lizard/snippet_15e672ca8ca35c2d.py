def _max_lengths():
    max_header_length = max([(len(x.byte_match) + x.offset) for x in
        magic_header_array])
    max_footer_length = max([(len(x.byte_match) + abs(x.offset)) for x in
        magic_footer_array])
    return max_header_length, max_footer_length