def _srels_for(phys_reader, source_uri):
    rels_xml = phys_reader.rels_xml_for(source_uri)
    return _SerializedRelationships.load_from_xml(source_uri.baseURI, rels_xml)