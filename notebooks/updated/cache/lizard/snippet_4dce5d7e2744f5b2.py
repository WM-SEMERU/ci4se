def buildcss(app, buildpath, imagefile):
    div = 'body'
    repeat = 'repeat-y'
    position = 'center'
    attachment = 'scroll'
    if app.config.sphinxmark_div != 'default':
        div = app.config.sphinxmark_div
    if app.config.sphinxmark_repeat is False:
        repeat = 'no-repeat'
    if app.config.sphinxmark_fixed is True:
        attachment = 'fixed'
    border = app.config.sphinxmark_border
    if border == 'left' or border == 'right':
        css = template('border', div=div, image=imagefile, side=border)
    else:
        css = template('watermark', div=div, image=imagefile, repeat=repeat,
            position=position, attachment=attachment)
    LOG.debug('[sphinxmark] Template: ' + css)
    cssname = 'sphinxmark.css'
    cssfile = os.path.join(buildpath, cssname)
    with open(cssfile, 'w') as f:
        f.write(css)
    return cssname