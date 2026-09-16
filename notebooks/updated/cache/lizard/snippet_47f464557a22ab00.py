def serialize(self, subject, *objects_or_combinators):
    ec_s = rdflib.BNode()
    if self.operator is not None:
        if subject is not None:
            yield subject, self.predicate, ec_s
        yield from oc(ec_s)
        yield from self._list.serialize(ec_s, self.operator, *
            objects_or_combinators)
    else:
        for thing in objects_or_combinators:
            if isinstance(thing, Combinator):
                object = rdflib.BNode()
                hasType = False
                for t in thing(object):
                    if t[1] == rdf.type:
                        hasType = True
                    yield t
                if not hasType:
                    yield object, rdf.type, owl.Class
            else:
                object = thing
            yield subject, self.predicate, object