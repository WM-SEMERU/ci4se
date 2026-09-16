def _finalize_arguments(self, args):
    gps = args.gps
    search = args.search
    max_plot = max(args.plot)
    search = max(search, max_plot * 2 + 8)
    args.search = search
    self.log(3, 'Search window: {0:.0f} sec, max plot window {1:.0f}'.
        format(search, max_plot))
    xpix = 1200.0
    if args.geometry:
        m = re.match('(\\d+)x(\\d+)', args.geometry)
        if m:
            xpix = float(m.group(1))
    args.nx = xpix
    self.args.tres = search / xpix / 2
    self.log(3, 'Max time resolution (tres) set to {:.4f}'.format(self.args
        .tres))
    args.start = [[int(gps - search / 2)]]
    if args.epoch is None:
        args.epoch = args.gps
    args.duration = search
    args.chan = [[args.chan]]
    if args.color_scale is None:
        args.color_scale = 'linear'
    args.overlap = 0
    xmin = args.xmin
    xmax = args.xmax
    super(Qtransform, self)._finalize_arguments(args)
    args.xmin = xmin
    args.xmax = xmax