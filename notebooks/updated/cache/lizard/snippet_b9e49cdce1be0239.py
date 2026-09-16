def prt_nts(prt, nts, varname, spc='    '):
    first_nt = nts[0]
    nt_name = type(first_nt).__name__
    prt.write('import collections as cx\n\n')
    prt.write('NT_FIELDS = [\n')
    for fld in first_nt._fields:
        prt.write('{SPC}"{F}",\n'.format(SPC=spc, F=fld))
    prt.write(']\n\n')
    prt.write('{NtName} = cx.namedtuple("{NtName}", " ".join(NT_FIELDS))\n\n'
        .format(NtName=nt_name))
    prt.write('# {N:,} items\n'.format(N=len(nts)))
    prt.write('# pylint: disable=line-too-long\n')
    prt.write('{VARNAME} = [\n'.format(VARNAME=varname))
    for ntup in nts:
        prt.write('{SPC}{NT},\n'.format(SPC=spc, NT=ntup))
    prt.write(']\n')