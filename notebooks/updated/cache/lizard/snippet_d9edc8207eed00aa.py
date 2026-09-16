def store(self, obj):
    if type(obj) is AtlasServiceInstance.Instance:
        query = {'instance_id': obj.instance_id, 'database': obj.get_dbname
            (), 'cluster': obj.get_cluster(), 'parameters': obj.parameters}
    elif type(obj) is AtlasServiceBinding.Binding:
        query = {'binding_id': obj.binding_id, 'parameters': obj.parameters,
            'instance_id': obj.instance.instance_id}
    else:
        raise ErrStorageTypeUnsupported(type(obj))
    try:
        result = self.broker.insert_one(query)
    except:
        raise ErrStorageMongoConnection('Store Instance or Binding')
    if result is not None:
        obj.provisioned = True
        return result.inserted_id
    raise ErrStorageStore()