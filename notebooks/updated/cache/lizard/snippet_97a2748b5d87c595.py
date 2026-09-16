def _iter_channels(framefile):
    from LDAStools import frameCPP
    if not isinstance(framefile, frameCPP.IFrameFStream):
        framefile = open_gwf(framefile, 'r')
    toc = framefile.GetTOC()
    for typename in ('Sim', 'Proc', 'ADC'):
        typen = typename.lower()
        for name in getattr(toc, 'Get{0}'.format(typename))():
            yield name, typen