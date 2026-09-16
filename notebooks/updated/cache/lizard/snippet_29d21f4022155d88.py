def get_impl_ver(env):
    impl_ver = env.config_var('py_version_nodot')
    if not impl_ver or get_abbr_impl(env) == 'pp':
        impl_ver = ''.join(map(str, get_impl_version_info(env)))
    return impl_ver