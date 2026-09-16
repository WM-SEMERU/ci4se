def resolve(self, configurable=None, scope=None, safe=None, besteffort=None):
    if scope is None:
        scope = self.scope
    if safe is None:
        safe = self.safe
    if besteffort is None:
        besteffort = self.besteffort
    for category in self.values():
        for param in category.values():
            param.resolve(configurable=configurable, conf=self, scope=scope,
                safe=safe, besteffort=besteffort)