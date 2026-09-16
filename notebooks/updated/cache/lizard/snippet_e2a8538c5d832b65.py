def get_json_tree_path(self, *args, **kwargs):
    json_tree_path = os.path.join(self.TREES_DATA_DIR, self.
        RICECOOKER_JSON_TREE)
    return json_tree_path