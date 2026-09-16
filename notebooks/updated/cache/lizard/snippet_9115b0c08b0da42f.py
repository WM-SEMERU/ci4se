async def read(cls, fabric: Union[Fabric, int], vid: int):
    if isinstance(fabric, int):
        fabric_id = fabric
    elif isinstance(fabric, Fabric):
        fabric_id = fabric.id
    else:
        raise TypeError('fabric must be a Fabric or int, not %s' % type(
            fabric).__name__)
    data = await cls._handler.read(fabric_id=fabric_id, vid=vid)
    return cls(data, {'fabric_id': fabric_id})