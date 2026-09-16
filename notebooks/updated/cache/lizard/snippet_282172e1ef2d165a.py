def _parse_coords(self, opts):
    if 'coords' in vars(opts):
        return
    radius = vars(opts).get('radius', 0)
    gal = None
    if vars(opts).get('gal') is not None:
        gal = opts.gal
    elif vars(opts).get('cel') is not None:
        gal = cel2gal(*opts.cel)
    elif vars(opts).get('hpx') is not None:
        gal = pix2ang(*opts.hpx)
    if gal is not None:
        opts.coords = [(gal[0], gal[1], radius)]
        opts.names = [vars(opts).get('name', '')]
    else:
        opts.coords = None
        opts.names = None
    if vars(opts).get('targets') is not None:
        opts.names, opts.coords = self.parse_targets(opts.targets)
        if vars(opts).get('radius') is not None:
            opts.coords['radius'] = vars(opts).get('radius')