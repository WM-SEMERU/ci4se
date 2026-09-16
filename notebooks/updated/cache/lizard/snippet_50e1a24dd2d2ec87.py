def new_actuator(joint, act_type='actuator', **kwargs):
    element = ET.Element(act_type, attrib=kwargs)
    element.set('joint', joint)
    return element