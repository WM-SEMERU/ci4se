def is_quote_artifact(orig_text, span):
    res = False
    cursor = re.finditer('("|\\\')[^ .,:;?!()*+-].*?("|\\\')', orig_text)
    for item in cursor:
        if item.span()[1] == span[1]:
            res = True
    return res