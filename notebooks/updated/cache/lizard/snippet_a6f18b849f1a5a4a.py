def _SlidePlaceholderFactory(shape_elm, parent):
    tag = shape_elm.tag
    if tag == qn('p:sp'):
        Constructor = {PP_PLACEHOLDER.BITMAP: PicturePlaceholder,
            PP_PLACEHOLDER.CHART: ChartPlaceholder, PP_PLACEHOLDER.PICTURE:
            PicturePlaceholder, PP_PLACEHOLDER.TABLE: TablePlaceholder}.get(
            shape_elm.ph_type, SlidePlaceholder)
    elif tag == qn('p:graphicFrame'):
        Constructor = PlaceholderGraphicFrame
    elif tag == qn('p:pic'):
        Constructor = PlaceholderPicture
    else:
        Constructor = BaseShapeFactory
    return Constructor(shape_elm, parent)