def compile_authors(cell):
    logger_excel.info('enter compile_authors')
    author_lst = []
    s = cell.split(';')
    for w in s:
        author_lst.append(w.lstrip())
    logger_excel.info('exit compile_authors')
    return author_lst