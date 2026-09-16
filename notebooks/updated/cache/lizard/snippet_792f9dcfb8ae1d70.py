def load_collided_alias(self):
    open_mode = 'r+' if os.path.exists(GLOBAL_COLLIDED_ALIAS_PATH) else 'w+'
    with open(GLOBAL_COLLIDED_ALIAS_PATH, open_mode) as collided_alias_file:
        collided_alias_str = collided_alias_file.read()
        try:
            self.collided_alias = json.loads(collided_alias_str if
                collided_alias_str else '{}')
        except Exception:
            self.collided_alias = {}