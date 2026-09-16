def from_model(cls, document):
    return cls(meta={'id': document.id}, **cls.serialize(document))