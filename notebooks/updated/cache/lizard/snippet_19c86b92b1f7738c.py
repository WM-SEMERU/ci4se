def BaseShapeFactory(shape_elm, parent):
    tag = shape_elm.tag
    if tag == qn('p:pic'):
        videoFiles = shape_elm.xpath('./p:nvPicPr/p:nvPr/a:videoFile')
        if videoFiles:
            return Movie(shape_elm, parent)
        return Picture(shape_elm, parent)
    shape_cls = {qn('p:cxnSp'): Connector, qn('p:grpSp'): GroupShape, qn(
        'p:sp'): Shape, qn('p:graphicFrame'): GraphicFrame}.get(tag, BaseShape)
    return shape_cls(shape_elm, parent)