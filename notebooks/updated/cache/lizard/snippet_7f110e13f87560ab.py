def _fake_referencenames(self, namespace, **params):
    assert params['ResultClass'] is None or isinstance(params['ResultClass'
        ], CIMClassName)
    rc = None if params['ResultClass'] is None else params['ResultClass'
        ].classname
    role = params['Role']
    obj_name = params['ObjectName']
    classname = obj_name.classname
    if isinstance(obj_name, CIMClassName):
        ref_classnames = self._get_reference_classnames(classname,
            namespace, rc, role)
        ref_result = [CIMClassName(classname=cn, host=self.host, namespace=
            namespace) for cn in ref_classnames]
        return self._return_assoc_tuple(ref_result)
    assert isinstance(obj_name, CIMInstanceName)
    ref_paths = self._get_reference_instnames(obj_name, namespace, rc, role)
    rtn_names = [deepcopy(r) for r in ref_paths]
    for iname in rtn_names:
        if iname.host is None:
            iname.host = self.host
    return self._return_assoc_tuple(rtn_names)