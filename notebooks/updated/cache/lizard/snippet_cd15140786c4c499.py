def validate_env(self, envname):
    if self.whitelist_envs and envname in self.whitelist_envs:
        return True
    elif self.whitelist_envs:
        return False
    if self.blacklist_envs and envname not in self.blacklist_envs:
        return True
    elif self.blacklist_envs:
        return False
    else:
        return True