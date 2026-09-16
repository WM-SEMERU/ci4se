def publish(dataset_uri):
    try:
        dataset = dtoolcore.DataSet.from_uri(dataset_uri)
    except dtoolcore.DtoolCoreTypeError:
        print('Not a dataset: {}'.format(dataset_uri))
        sys.exit(1)
    try:
        access_uri = dataset._storage_broker.http_enable()
    except AttributeError:
        print("Datasets of type '{}' cannot be published using HTTP".format
            (dataset._storage_broker.key))
        sys.exit(2)
    return access_uri