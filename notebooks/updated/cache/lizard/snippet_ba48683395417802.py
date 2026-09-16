def get_parcel(resource_root, product, version, cluster_name='default'):
    return _get_parcel(resource_root, PARCEL_PATH % (cluster_name, product,
        version))