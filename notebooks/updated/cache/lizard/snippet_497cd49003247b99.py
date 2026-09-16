def sheet_asdict(fn, sheet=0, header=True, startcell=None, stopcell=None,
    usecols=None, chnames_out=None):
    book = xlrd.open_workbook(fn)
    try:
        sh = book.sheet_by_index(sheet)
    except TypeError:
        sh = book.sheet_by_name(sheet)
    ss = prepread(sh, header=header, startcell=startcell, stopcell=stopcell)
    chnames = sheetheader(sh, ss, usecols=usecols)
    if chnames_out is not None and chnames is not None:
        vals = list(chnames_out)
        [chnames_out.remove(v) for v in vals]
        chnames_out.extend(chnames)
    return _sheet_asdict(sh, ss, usecols=usecols)