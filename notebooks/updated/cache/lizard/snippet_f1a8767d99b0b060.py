def delete_instance(self, credentials, name, **kwargs):
    op_name = delete_instance(credentials, self.project, self.zone, name,
        **kwargs)
    return op_name