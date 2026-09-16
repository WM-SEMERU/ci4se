def convert(filepath, outfilepath):
    logger = logging.getLogger('example1')
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter(STD_FORMAT)
    stderrHdlr = logging.StreamHandler()
    stderrHdlr.setFormatter(fmt)
    logger.addHandler(stderrHdlr)
    fi = ImageViewCairo(logger)
    fi.configure(500, 1000)
    image = load_data(filepath, logger=logger)
    fi.set_bg(1.0, 1.0, 1.0)
    fi.set_image(image)
    fi.auto_levels()
    fi.zoom_fit()
    fi.center_image()
    ht_pts = 11.0 / point_in
    wd_pts = 8.5 / point_in
    off_x, off_y = 0, 0
    out_f = open(outfilepath, 'w')
    surface = cairo.PDFSurface(out_f, wd_pts, ht_pts)
    surface.set_fallback_resolution(300, 300)
    surface.set_device_offset(off_x, off_y)
    try:
        fi.save_image_as_surface(surface)
        surface.show_page()
        surface.flush()
        surface.finish()
    finally:
        out_f.close()