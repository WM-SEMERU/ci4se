def compute_json(self, build_context):
    props = {}
    test_props = {}
    for prop in self.props:
        if prop in self._prop_json_blacklist:
            continue
        sig_spec = Plugin.builders[self.builder_name].sig.get(prop)
        if sig_spec is None:
            continue
        if prop in self._prop_json_testlist:
            test_props[prop] = process_prop(sig_spec.type, self.props[prop],
                build_context)
        else:
            props[prop] = process_prop(sig_spec.type, self.props[prop],
                build_context)
    json_dict = dict(name=self.name, builder_name=self.builder_name, deps=
        hashify_targets(self.deps, build_context), props=props, buildenv=
        hashify_targets(self.buildenv, build_context), tags=sorted(list(
        self.tags)), flavor=build_context.conf.flavor)
    json_test_dict = dict(props=test_props)
    self._json = json.dumps(json_dict, sort_keys=True, indent=4)
    self._test_json = json.dumps(json_test_dict, sort_keys=True, indent=4)