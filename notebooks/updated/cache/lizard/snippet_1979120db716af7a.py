def server_info(self, session=None):
    return self.admin.command('buildinfo', read_preference=ReadPreference.
        PRIMARY, session=session)