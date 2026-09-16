def new(cls, rId, reltype, target, target_mode=RTM.INTERNAL):
    xml = '<Relationship xmlns="%s"/>' % nsmap['pr']
    relationship = parse_xml(xml)
    relationship.rId = rId
    relationship.reltype = reltype
    relationship.target_ref = target
    relationship.targetMode = target_mode
    return relationship