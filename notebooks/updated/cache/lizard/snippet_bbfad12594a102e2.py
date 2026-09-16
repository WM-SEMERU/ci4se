async def uint(self, elem, elem_type, params=None):
    if self.writing:
        return IntegerModel(elem, elem_type.WIDTH) if self.modelize else elem
    else:
        return elem.val if isinstance(elem, IModel) else elem