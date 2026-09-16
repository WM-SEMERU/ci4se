def build_provider(self, stack):
    return self.provider_builder.build(region=stack.region, profile=stack.
        profile)