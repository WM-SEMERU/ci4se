def get_os_version_codename(codename, version_map=OPENSTACK_CODENAMES):
    for k, v in six.iteritems(version_map):
        if v == codename:
            return k
    e = 'Could not derive OpenStack version for codename: %s' % codename
    error_out(e)