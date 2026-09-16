def get_objanno(fin_anno, anno_type=None, **kws):
    anno_type = get_anno_desc(fin_anno, anno_type)
    if anno_type is not None:
        if anno_type == 'gene2go':
            return Gene2GoReader(fin_anno, **kws)
        if anno_type == 'gaf':
            return GafReader(fin_anno, hdr_only=kws.get('hdr_only', False),
                prt=kws.get('prt', sys.stdout), allow_missing_symbol=kws.
                get('allow_missing_symbol', False))
        if anno_type == 'gpad':
            hdr_only = kws.get('hdr_only', False)
            return GpadReader(fin_anno, hdr_only)
        if anno_type == 'id2gos':
            return IdToGosReader(fin_anno)
    raise RuntimeError('UNEXPECTED ANNOTATION FILE FORMAT: {F} {D}'.format(
        F=fin_anno, D=anno_type))