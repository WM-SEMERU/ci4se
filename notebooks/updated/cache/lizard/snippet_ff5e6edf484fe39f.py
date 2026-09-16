def save_metadata(self, profile='default'):
    if len(self.tables) > 0:
        f = profile_path(DBPY_PROFILE_ID, profile)
        dump_to_json(f, self.to_dict())