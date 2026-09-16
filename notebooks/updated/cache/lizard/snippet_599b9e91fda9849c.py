def GetNewSessionID(self, **_):
    return rdfvalue.SessionID(base='aff4:/hunts', queue=self.runner_args.queue)