def to_profile_info(self, serialize_credentials=False):
    result = {'profile_name': self.profile_name, 'target_name': self.
        target_name, 'config': self.config.to_dict(), 'threads': self.
        threads, 'credentials': self.credentials.incorporate()}
    if serialize_credentials:
        result['credentials'] = result['credentials'].serialize()
    return result