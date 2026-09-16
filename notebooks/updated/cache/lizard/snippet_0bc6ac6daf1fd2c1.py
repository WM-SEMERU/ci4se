def ListFlows(self):
    args = flow_pb2.ApiListFlowsArgs(client_id=self.client_id)
    items = self._context.SendIteratorRequest('ListFlows', args)
    return utils.MapItemsIterator(lambda data: flow.Flow(data=data, context
        =self._context), items)