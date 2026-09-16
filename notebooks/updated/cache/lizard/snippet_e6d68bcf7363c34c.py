def parse_doc_dict(text=None, split_character='::'):
    text = text or function_doc(2)
    text = text.split(split_character, 1)[-1]
    text = text.split(':param')[0].split(':return')[0]
    text = text.strip().split('\n')

    def clean(t):
        return t.split(':', 1)[0].strip(), t.split(':', 1)[1].strip()
    return dict(clean(line) for line in text)