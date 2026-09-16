def _check_infinite_flows(self, steps, flows=None):
    if flows is None:
        flows = []
    for step in steps.values():
        if 'flow' in step:
            flow = step['flow']
            if flow == 'None':
                continue
            if flow in flows:
                raise FlowInfiniteLoopError(
                    'Infinite flows detected with flow {}'.format(flow))
            flows.append(flow)
            flow_config = self.project_config.get_flow(flow)
            self._check_infinite_flows(flow_config.steps, flows)