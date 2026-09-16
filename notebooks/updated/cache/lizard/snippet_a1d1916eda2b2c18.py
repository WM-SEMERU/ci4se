def put(cls, obj):
    return PyarrowOnRayFramePartition(ray.put(pyarrow.Table.from_pandas(obj)))