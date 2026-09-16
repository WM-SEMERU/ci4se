def notescan_main(options):
    filenames = get_filenames(options)
    outputs = []
    do_global = options.global_palette and len(filenames) > 1
    if do_global:
        filenames, palette = get_global_palette(filenames, options)
    do_postprocess = bool(options.postprocess_cmd)
    for input_filename in filenames:
        img, dpi = load(input_filename)
        if img is None:
            continue
        output_filename = '{}{:04d}.png'.format(options.basename, len(outputs))
        if not options.quiet:
            print('opened', input_filename)
        if not do_global:
            samples = sample_pixels(img, options)
            palette = get_palette(samples, options)
        labels = apply_palette(img, palette, options)
        save(output_filename, labels, palette, dpi, options)
        if do_postprocess:
            post_filename = postprocess(output_filename, options)
            if post_filename:
                output_filename = post_filename
            else:
                do_postprocess = False
        outputs.append(output_filename)
        if not options.quiet:
            print('  done\n')
    emit_pdf(outputs, options)