def recipe(recipe):
    env.host_string = lib.get_env_host_string()
    lib.print_header("Applying recipe '{0}' on node {1}".format(recipe, env
        .host_string))
    data = lib.get_node(env.host_string)
    data['run_list'] = ['recipe[{0}]'.format(recipe)]
    if not __testing__:
        if env.autodeploy_chef and not chef.chef_test():
            deploy_chef(ask='no')
        chef.sync_node(data)