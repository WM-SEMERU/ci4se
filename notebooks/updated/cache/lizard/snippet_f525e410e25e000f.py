def snip_string_middle(string, max_len=20, snip_string='...'):
    if len(string) <= max_len:
        new_string = string
    else:
        visible_len = max_len - len(snip_string)
        start_len = visible_len // 2
        end_len = visible_len - start_len
        new_string = string[0:start_len] + snip_string + string[-end_len:]
    return new_string