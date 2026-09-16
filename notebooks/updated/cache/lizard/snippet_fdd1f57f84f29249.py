def to_swagger(self, bound_resource=None):
    response_def = _to_swagger(description=self.description, resource=
        bound_resource if self.resource is DefaultResource else self.resource)
    status = self.status if self.status == 'default' else self.status.value
    return status, response_def