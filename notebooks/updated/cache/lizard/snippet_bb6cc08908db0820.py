def import_diagram_and_plane_attributes(diagram_attributes,
    plane_attributes, diagram_element, plane_element):
    diagram_attributes[consts.Consts.id] = diagram_element.getAttribute(consts
        .Consts.id)
    diagram_attributes[consts.Consts.name] = diagram_element.getAttribute(
        consts.Consts.name) if diagram_element.hasAttribute(consts.Consts.name
        ) else ''
    plane_attributes[consts.Consts.id] = plane_element.getAttribute(consts.
        Consts.id)
    plane_attributes[consts.Consts.bpmn_element] = plane_element.getAttribute(
        consts.Consts.bpmn_element)