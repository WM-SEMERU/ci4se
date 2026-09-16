def make_file_system_tree(root_folder, _parent=None):
    root_node = Node(os.path.basename(root_folder), _parent)
    root_node.path = root_folder
    for item in os.listdir(root_folder):
        item_path = os.path.join(root_folder, item)
        if os.path.isfile(item_path):
            file_node = Node(os.path.basename(item), root_node)
            file_node.path = item_path
        elif os.path.isdir(item_path):
            make_file_system_tree(item_path, _parent=root_node)
    return root_node