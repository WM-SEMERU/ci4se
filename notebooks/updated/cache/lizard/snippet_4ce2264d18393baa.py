def user_create(auth=None, **kwargs):
    cloud = get_openstack_cloud(auth)
    kwargs = _clean_kwargs(keep_name=True, **kwargs)
    return cloud.create_user(**kwargs)