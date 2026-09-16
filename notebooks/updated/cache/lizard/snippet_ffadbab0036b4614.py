def run(self):
    if self.workflow.builder.base_from_scratch:
        self.log.info(
            'Skipping comparing components: unsupported for FROM-scratch images'
            )
        return
    worker_metadatas = self.workflow.postbuild_results.get(
        PLUGIN_FETCH_WORKER_METADATA_KEY)
    comp_list = self.get_component_list_from_workers(worker_metadatas)
    if not comp_list:
        raise ValueError('No components to compare')
    package_comparison_exceptions = get_package_comparison_exceptions(self.
        workflow)
    master_comp = {}
    failed_components = set()
    for components in comp_list:
        for component in components:
            t = component['type']
            name = component['name']
            if name in package_comparison_exceptions:
                self.log.info('Ignoring comparison of package %s', name)
                continue
            if t not in SUPPORTED_TYPES:
                raise ValueError('Type %s not supported' % t)
            if name in failed_components:
                continue
            identifier = t, name
            if identifier not in master_comp:
                master_comp[identifier] = component
                continue
            if t == T_RPM:
                mc = master_comp[identifier]
                try:
                    self.rpm_compare(mc, component)
                except ValueError as ex:
                    self.log.debug('Mismatch details: %s', ex)
                    self.log.warning('Comparison mismatch for component %s:',
                        name)
                    for comp in filter_components_by_name(name, comp_list):
                        self.log_rpm_component(comp)
                    failed_components.add(name)
    if failed_components:
        raise ValueError(
            'Failed component comparison for components: {components}'.
            format(components=', '.join(sorted(failed_components))))