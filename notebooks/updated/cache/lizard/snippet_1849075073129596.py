def _list_cmaps(provider=None, records=False):
    if provider is None:
        provider = providers
    elif isinstance(provider, basestring):
        if provider not in providers:
            raise ValueError(
                'Colormap provider %r not recognized, must be one of %r' %
                (provider, providers))
        provider = [provider]
    cmaps = []

    def info(provider, names):
        return [CMapInfo(name=n, provider=provider, category=None, source=
            None, bg=None) for n in names] if records else list(names)
    if 'matplotlib' in provider:
        try:
            import matplotlib.cm as cm
            cmaps += info('matplotlib', [cmap for cmap in cm.cmap_d if not
                (cmap.startswith('cet_') or cmap.startswith('Vega') or cmap
                .startswith('spectral'))])
        except:
            pass
    if 'bokeh' in provider:
        try:
            from bokeh import palettes
            cmaps += info('bokeh', palettes.all_palettes)
            cmaps += info('bokeh', [(p + '_r') for p in palettes.all_palettes])
        except:
            pass
    if 'colorcet' in provider:
        try:
            from colorcet import palette_n, glasbey_hv
            cet_maps = palette_n.copy()
            cet_maps['glasbey_hv'] = glasbey_hv
            cmaps += info('colorcet', cet_maps)
            cmaps += info('colorcet', [(p + '_r') for p in cet_maps])
        except:
            pass
    return sorted(unique_iterator(cmaps))