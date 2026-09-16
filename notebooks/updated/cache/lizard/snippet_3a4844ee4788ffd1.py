def orient_page(infiles, output_file, log, context):
    options = context.get_options()
    page_pdf = next(ii for ii in infiles if ii.endswith('.page.pdf'))
    if not options.rotate_pages:
        re_symlink(page_pdf, output_file, log)
        return
    preview = next(ii for ii in infiles if ii.endswith('.preview.jpg'))
    orient_conf = tesseract.get_orientation(preview, engine_mode=options.
        tesseract_oem, timeout=options.tesseract_timeout, log=log)
    direction = {(0): '⇧', (90): '⇨', (180): '⇩', (270): '⇦'}
    pageno = page_number(page_pdf) - 1
    pdfinfo = context.get_pdfinfo()
    existing_rotation = pdfinfo[pageno].rotation
    correction = orient_conf.angle % 360
    apply_correction = False
    action = ''
    if orient_conf.confidence >= options.rotate_pages_threshold:
        if correction != 0:
            apply_correction = True
            action = ' - will rotate'
        else:
            action = ' - rotation appears correct'
    elif correction != 0:
        action = ' - confidence too low to rotate'
    else:
        action = ' - no change'
    facing = ''
    if existing_rotation != 0:
        facing = 'with existing rotation {}, '.format(direction.get(
            existing_rotation, '?'))
    facing += 'page is facing {}'.format(direction.get(orient_conf.angle, '?'))
    log.info('{pagenum:4d}: {facing}, confidence {conf:.2f}{action}'.format
        (pagenum=page_number(preview), facing=facing, conf=orient_conf.
        confidence, action=action))
    re_symlink(page_pdf, output_file, log)
    if apply_correction:
        context.set_rotation(pageno, correction)