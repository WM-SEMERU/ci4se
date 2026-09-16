def load_adjustment_values():
    thisdir = os.path.split(__file__)[0]
    prst_defs_relpath = (
        'ISO-IEC-29500-1/schemas/dml-geometries/OfficeOpenXML-DrawingMLGeometries/presetShapeDefinitions.xml'
        )
    prst_defs_path = os.path.join(thisdir, prst_defs_relpath)
    presetShapeDefinitions = objectify.parse(prst_defs_path).getroot()
    ns = 'http://schemas.openxmlformats.org/drawingml/2006/main'
    avLst_qn = '{%s}avLst' % ns
    adjustment_values = []
    for shapedef in presetShapeDefinitions.iterchildren():
        prst = shapedef.tag
        try:
            avLst = shapedef[avLst_qn]
        except AttributeError:
            continue
        for idx, gd in enumerate(avLst.gd):
            name = gd.get('name')
            val = int(gd.get('fmla')[4:])
            record = prst, idx + 1, name, val
            adjustment_values.append(record)
    return adjustment_values