def content():
    message = m.Message()
    paragraph = m.Paragraph(m.Image(
        'file:///%s/img/screenshots/shakemap-converter-screenshot.png' %
        resources_path()), style_class='text-center')
    message.add(paragraph)
    body = tr(
        "This tool will convert an earthquake 'shakemap' that is in grid xml format into a GeoTIFF file. The imported file can be used in InaSAFE as an input for impact functions that require an earthquake layer.  To use this tool effectively:"
        )
    message.add(body)
    tips = m.BulletedList()
    tips.add(tr('Select a grid.xml for the input layer.'))
    tips.add(tr('Choose where to write the output layer to.'))
    tips.add(tr(
        'Choose the interpolation algorithm that should be used when converting the xml grid to a raster. If unsure keep the default.'
        ))
    tips.add(tr(
        'If you want to obtain shake data you can get download it free from the USGS shakemap site: http://earthquake.usgs.gov/earthquakes/shakemap/list.php?y=2013'
        ))
    message.add(tips)
    return message