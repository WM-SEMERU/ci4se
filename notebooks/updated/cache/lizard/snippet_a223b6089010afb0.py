def execute(self, triple_map, output, **kwargs):
    subjects = []
    logical_src_iterator = str(triple_map.logicalSource.iterator)
    json_object = kwargs.get('obj', self.source)
    if logical_src_iterator == '.':
        results = [None]
    else:
        json_path_exp = jsonpath_ng.parse(logical_src_iterator)
        results = [r.value for r in json_path_exp.find(json_object)][0]
    for row in results:
        subject = self.generate_term(term_map=triple_map.subjectMap, **kwargs)
        for pred_obj_map in triple_map.predicateObjectMap:
            predicate = pred_obj_map.predicate
            if pred_obj_map.template is not None:
                output.add((subject, predicate, self.generate_term(term_map
                    =pred_obj_map, **kwargs)))
            if pred_obj_map.parentTriplesMap is not None:
                self.__handle_parents__(output, parent_map=pred_obj_map.
                    parentTriplesMap, subject=subject, predicate=predicate,
                    obj=row, **kwargs)
            if pred_obj_map.reference is not None:
                ref_exp = jsonpath_ng.parse(str(pred_obj_map.reference))
                found_objects = [r.value for r in ref_exp.find(row)]
                for obj in found_objects:
                    if rdflib.term._is_valid_uri(obj):
                        rdf_obj = rdflib.URIRef(str(obj))
                    else:
                        rdf_obj = rdflib.Literal(str(obj))
                    output.add((subject, predicate, rdf_obj))
            if pred_obj_map.constant is not None:
                output.add((subject, predicate, pred_obj_map.constant))
        subjects.append(subject)
    return subjects