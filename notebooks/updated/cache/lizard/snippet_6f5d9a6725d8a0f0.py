def auto_detect_adjacent_shapes(svg_source, shape_i_attr='id', layer_name=
    'Connections', shapes_xpath='//svg:path | //svg:polygon', extend=1.5):
    df_shapes = svg_shapes_to_df(svg_source, xpath=shapes_xpath)
    df_shapes = compute_shape_centers(df_shapes, shape_i_attr)
    df_shape_connections = extract_adjacent_shapes(df_shapes, shape_i_attr,
        extend=extend)
    xml_root = etree.parse(svg_source)
    svg_root = xml_root.xpath('/svg:svg', namespaces=INKSCAPE_NSMAP)[0]
    df_shape_centers = df_shapes.drop_duplicates(subset=[shape_i_attr])[[
        shape_i_attr] + ['x_center', 'y_center']].set_index(shape_i_attr)
    df_connection_centers = df_shape_centers.loc[df_shape_connections.source
        ].reset_index(drop=True).join(df_shape_centers.loc[
        df_shape_connections.target].reset_index(drop=True), lsuffix=
        '_source', rsuffix='_target')
    connections_xpath = '//svg:g[@inkscape:label="%s"]' % layer_name
    connections_groups = svg_root.xpath(connections_xpath, namespaces=
        INKSCAPE_NSMAP)
    if connections_groups:
        for g in connections_groups:
            g.getparent().remove(g)
    svg_output = draw_lines_svg_layer(df_connection_centers.rename(columns=
        {'x_center_source': 'x_source', 'y_center_source': 'y_source',
        'x_center_target': 'x_target', 'y_center_target': 'y_target'}),
        layer_name=layer_name)
    return svg_output