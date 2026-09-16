async def container_dump(self, container, container_type, params=None, obj=None
    ):
    elem_type = x.container_elem_type(container_type, params)
    obj = [] if not x.has_elem(obj) else x.get_elem(obj)
    if container is None:
        return NoSetSentinel()
    for idx, elem in enumerate(container):
        try:
            self.tracker.push_index(idx)
            fvalue = await self._dump_field(elem, elem_type, params[1:] if
                params else None)
            self.tracker.pop()
        except Exception as e:
            raise helpers.ArchiveException(e, tracker=self.tracker) from e
        if not isinstance(fvalue, NoSetSentinel):
            obj.append(fvalue)
    return obj if not self.modelize else ArrayModel(obj, xmr_type_to_type(
        elem_type))