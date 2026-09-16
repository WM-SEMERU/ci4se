def to_dict(self, properties=None):
    if not properties:
        properties = [p for p in dir(Assay) if isinstance(getattr(Assay, p),
            property)]
    return {p: getattr(self, p) for p in properties}