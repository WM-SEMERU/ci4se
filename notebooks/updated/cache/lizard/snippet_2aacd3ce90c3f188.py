def get_all_services(resource_root, cluster_name='default', view=None):
    return call(resource_root.get, SERVICES_PATH % (cluster_name,),
        ApiService, True, params=view and dict(view=view) or None)