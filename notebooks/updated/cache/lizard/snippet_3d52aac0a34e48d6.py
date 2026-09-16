def _fake_associators(self, namespace, **params):
    self._validate_namespace(namespace)
    rc = None if params['ResultClass'] is None else params['ResultClass'
        ].classname
    ac = None if params['AssocClass'] is None else params['AssocClass'
        ].classname
    role = params['Role']
    result_role = params['ResultRole']
    obj_name = params['ObjectName']
    classname = obj_name.classname
    pl = params['PropertyList']
    ico = params['IncludeClassOrigin']
    iq = params['IncludeQualifiers']
    if isinstance(obj_name, CIMClassName):
        rtn_classnames = self._get_associated_classnames(classname,
            namespace, ac, rc, result_role, role)
        return self._return_assoc_class_tuples(rtn_classnames, namespace,
            iq, ico, pl)
    assert isinstance(obj_name, CIMInstanceName)
    assoc_names = self._get_associated_instancenames(obj_name, namespace,
        ac, rc, result_role, role)
    results = []
    for obj_name in assoc_names:
        results.append(self._get_instance(obj_name, namespace, None, params
            ['PropertyList'], params['IncludeClassOrigin'], params[
            'IncludeQualifiers']))
    return self._return_assoc_tuple(results)