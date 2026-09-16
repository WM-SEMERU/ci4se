def parse_names(lstfile):
    from jcvi.formats.base import read_block
    fp = open(lstfile)
    all_authors = []
    for header, seq in read_block(fp, '['):
        seq = ' '.join(seq)
        authors = []
        for au in seq.split(','):
            au = au.strip()
            if not au:
                continue
            au = string.translate(au, None, string.digits)
            authors.append(au)
        all_authors.append(authors)
    out = []
    for authors in all_authors:
        blocks = []
        for au in authors:
            last, first, initials = get_name_parts(au)
            suffix = ''
            nameblock = NameTemplate.format(last=last, first=first,
                initials=initials, suffix=suffix)
            blocks.append(nameblock)
        bigblock = ',\n'.join(blocks)
        out.append(bigblock)
    return out