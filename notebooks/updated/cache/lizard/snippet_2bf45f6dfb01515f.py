def generate_security_data(self):
    timestamp = int(time.time())
    security_dict = {'content_type': str(self.target_object._meta),
        'object_pk': str(self.target_object._get_pk_val()), 'timestamp':
        str(timestamp), 'security_hash': self.initial_security_hash(timestamp)}
    return security_dict