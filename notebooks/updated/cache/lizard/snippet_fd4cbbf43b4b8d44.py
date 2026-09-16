def load_from_xml(baseURI, rels_item_xml):
    srels = _SerializedRelationshipCollection()
    if rels_item_xml is not None:
        rels_elm = parse_xml(rels_item_xml)
        for rel_elm in rels_elm.relationship_lst:
            srels._srels.append(_SerializedRelationship(baseURI, rel_elm))
    return srels