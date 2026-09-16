def GetNodeStorageUnits(r, node, storage_type, output_fields):
    query = {'storage_type': storage_type, 'output_fields': output_fields}
    return r.request('get', '/2/nodes/%s/storage' % node, query=query)