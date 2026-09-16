def _assoc_prop_matches(prop, ref_classname, assoc_classes, result_classes,
    result_role):
    assert prop.type == 'reference'
    if assoc_classes and ref_classname not in assoc_classes:
        return False
    if result_classes and prop.reference_class not in result_classes:
        return False
    if result_role and prop.name.lower() != result_role:
        return False
    return True