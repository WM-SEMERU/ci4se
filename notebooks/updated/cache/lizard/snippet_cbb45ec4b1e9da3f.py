def _canonicalize_query(self, query):

    def transform_query(q):
        for encoder in self.query_encoders:
            q = encoder.encode(q, [])
        if isinstance(q, dict):
            nq = {}
            for key, value in q.items():
                new_key = key
                if isinstance(value, dict) and len(value) == 1 and list(value
                    .keys())[0].startswith('$'):
                    if list(value.keys())[0] in ('$all', '$in'):
                        if list(value.values())[0] and isinstance(list(
                            value.values())[0][0], Document):
                            if self._use_pk_based_refs:
                                new_key += '.pk'
                            else:
                                new_key += '.__ref__'
                elif isinstance(value, Document):
                    if self._use_pk_based_refs:
                        new_key += '.pk'
                    else:
                        new_key += '.__ref__'
                nq[new_key] = transform_query(value)
            return nq
        elif isinstance(q, (list, QuerySet, tuple)):
            return [transform_query(x) for x in q]
        elif isinstance(q, Document):
            collection = self.get_collection_for_obj(q)
            if self._use_pk_based_refs:
                return q.pk
            else:
                return '%s:%s' % (collection, q.pk)
        else:
            return q
    return transform_query(query)