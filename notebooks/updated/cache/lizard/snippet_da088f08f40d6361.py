def inline_bbl(root_tex, bbl_tex):
    bbl_tex = bbl_tex.replace('\\', '\\\\')
    result = bib_pattern.sub(bbl_tex, root_tex)
    return result