def Get(self):
    args = hunt_pb2.ApiGetHuntArgs(hunt_id=self.hunt_id)
    data = self._context.SendRequest('GetHunt', args)
    return Hunt(data=data, context=self._context)