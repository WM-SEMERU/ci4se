def describe_underlying_workflow(self, region, describe_output=None):
    assert describe_output is None or describe_output.get('class', ''
        ) == 'globalworkflow'
    if region is None:
        raise DXError(
            'DXGlobalWorkflow: region must be provided to get an underlying workflow'
            )
    if region in self._workflow_desc_by_region:
        return self._workflow_desc_by_region[region]
    if not describe_output:
        describe_output = self.describe()
    if region not in describe_output['regionalOptions'].keys():
        raise DXError(
            'DXGlobalWorkflow: the global workflow {} is not enabled in region {}'
            .format(self.get_id(), region))
    underlying_workflow_id = describe_output['regionalOptions'][region][
        'workflow']
    dxworkflow = dxpy.DXWorkflow(underlying_workflow_id)
    dxworkflow_desc = dxworkflow.describe()
    self._workflow_desc_by_region = dxworkflow_desc
    return dxworkflow_desc