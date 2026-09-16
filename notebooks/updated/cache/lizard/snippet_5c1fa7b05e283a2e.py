def _remove_remote_node_data_bag():
    node_data_bag_path = os.path.join(env.node_work_path, 'data_bags', 'node')
    if exists(node_data_bag_path):
        sudo('rm -rf {0}'.format(node_data_bag_path))