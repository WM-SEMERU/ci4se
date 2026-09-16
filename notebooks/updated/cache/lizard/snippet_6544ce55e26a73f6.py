def add_authorizers(self, authorizers):
    self.security_definitions = self.security_definitions or {}
    for authorizer_name, authorizer in authorizers.items():
        self.security_definitions[authorizer_name
            ] = authorizer.generate_swagger()