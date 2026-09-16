def retrieve(self, node):
    if not self.is_enabled():
        return False
    env = node.get_build_env()
    if cache_show:
        if CacheRetrieveSilent(node, [], env, execute=1) == 0:
            node.build(presub=0, execute=0)
            return True
    elif CacheRetrieve(node, [], env, execute=1) == 0:
        return True
    return False