def _get_fields_for_class(schema_graph, graphql_types, field_type_overrides,
    hidden_classes, cls_name):
    properties = schema_graph.get_element_by_class_name(cls_name).properties
    all_properties = {property_name: _property_descriptor_to_graphql_type(
        property_obj) for property_name, property_obj in six.iteritems(
        properties)}
    result = {property_name: graphql_representation for property_name,
        graphql_representation in six.iteritems(all_properties) if 
        graphql_representation is not None}
    schema_element = schema_graph.get_element_by_class_name(cls_name)
    outbound_edges = (('out_{}'.format(out_edge_name), schema_graph.
        get_element_by_class_name(out_edge_name).properties[
        EDGE_DESTINATION_PROPERTY_NAME].qualifier) for out_edge_name in
        schema_element.out_connections)
    inbound_edges = (('in_{}'.format(in_edge_name), schema_graph.
        get_element_by_class_name(in_edge_name).properties[
        EDGE_SOURCE_PROPERTY_NAME].qualifier) for in_edge_name in
        schema_element.in_connections)
    for field_name, to_type_name in chain(outbound_edges, inbound_edges):
        edge_endpoint_type_name = None
        subclasses = schema_graph.get_subclass_set(to_type_name)
        to_type_abstract = schema_graph.get_element_by_class_name(to_type_name
            ).abstract
        if not to_type_abstract and len(subclasses) > 1:
            type_names_to_union = [subclass for subclass in subclasses if 
                subclass not in hidden_classes]
            if type_names_to_union:
                edge_endpoint_type_name = _get_union_type_name(
                    type_names_to_union)
        elif to_type_name not in hidden_classes:
            edge_endpoint_type_name = to_type_name
        if edge_endpoint_type_name is not None:
            result[field_name] = GraphQLList(graphql_types[
                edge_endpoint_type_name])
    for field_name, field_type in six.iteritems(field_type_overrides):
        if field_name not in result:
            raise AssertionError(
                'Attempting to override field "{}" from class "{}", but the class does not contain said field'
                .format(field_name, cls_name))
        else:
            result[field_name] = field_type
    return result