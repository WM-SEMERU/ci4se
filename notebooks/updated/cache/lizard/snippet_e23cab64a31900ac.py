def shape_type(self):
    if self.is_placeholder:
        return MSO_SHAPE_TYPE.PLACEHOLDER
    if self._sp.has_custom_geometry:
        return MSO_SHAPE_TYPE.FREEFORM
    if self._sp.is_autoshape:
        return MSO_SHAPE_TYPE.AUTO_SHAPE
    if self._sp.is_textbox:
        return MSO_SHAPE_TYPE.TEXT_BOX
    msg = 'Shape instance of unrecognized shape type'
    raise NotImplementedError(msg)