def load_children(self):
    children = list()
    statuses = list()
    version = None
    profiles = list()
    for element in self.xml_element:
        uri, tag = Element.get_namespace_and_tag(element.tag)
        if tag == 'version':
            if version is None:
                version = TailoringVersion(element)
            else:
                error_msg = 'version element found more than once'
                raise CardinalityException(error_msg)
        elif tag == 'status':
            statuses.append(Status(element))
        elif tag == 'Profile':
            profiles.append(Profile(element))
    if version is None:
        error_msg = 'version element is required'
        raise CardinalityException(error_msg)
    if len(profiles) <= 0:
        error_msg = 'Profile element is required at least once'
        raise CardinalityException(error_msg)
    children.extend(statuses)
    if version is not None:
        children.append(version)
    children.extend(profiles)
    return children