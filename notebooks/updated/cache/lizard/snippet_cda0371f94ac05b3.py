def migration(self, from_ver: int, to_ver: int):

    def decorator(func):
        migration = Migration(from_ver, to_ver, func)
        self.register_migration(migration)
        return func
    return decorator