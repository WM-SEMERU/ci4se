def create(self, project, email, role, **attrs):
    attrs.update({'project': project, 'email': email, 'role': role})
    return self._new_resource(payload=attrs)