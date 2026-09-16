def _segment_with_tokens(text, tokens):
    list_form = []
    text_ptr = 0
    for token in tokens:
        inter_token_string = []
        while not text[text_ptr:].startswith(token):
            inter_token_string.append(text[text_ptr])
            text_ptr += 1
            if text_ptr >= len(text):
                raise ValueError(
                    'Tokenization produced tokens that do not belong in string!'
                    )
        text_ptr += len(token)
        if inter_token_string:
            list_form.append(''.join(inter_token_string))
        list_form.append(token)
    if text_ptr < len(text):
        list_form.append(text[text_ptr:])
    return list_form