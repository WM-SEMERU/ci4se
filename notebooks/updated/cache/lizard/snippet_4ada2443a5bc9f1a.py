def get_single(self, key, lang=None):
    if not isinstance(key, URIRef):
        key = URIRef(key)
    if lang is not None:
        default = None
        for o in self.graph.objects(self.asNode(), key):
            default = o
            if o.language == lang:
                return o
        return default
    else:
        for o in self.graph.objects(self.asNode(), key):
            return o