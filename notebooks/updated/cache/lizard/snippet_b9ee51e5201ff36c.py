def histogram(numberfile, vmin, vmax, xlabel, title, outfmt='pdf', bins=50,
    skip=0, col=0, ascii=False, base=0, fill='white'):
    if ascii:
        return texthistogram([numberfile], vmin, vmax, title=title, bins=
            bins, skip=skip, col=col, base=base)
    data, vmin, vmax = get_data(numberfile, vmin, vmax, skip=skip, col=col)
    outfile = numberfile + '.base{0}.{1}'.format(base, outfmt
        ) if base else numberfile + '.pdf'
    template = histogram_log_template if base else histogram_template
    rtemplate = RTemplate(template, locals())
    rtemplate.run()