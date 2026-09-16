def resolve_domain(self, pipeline):
    domain = pipeline.domain(default=self._default_domain)
    if domain is GENERIC:
        raise ValueError(
            """Unable to determine domain for Pipeline.
Pass domain=<desired domain> to your Pipeline to set a domain."""
            )
    return domain