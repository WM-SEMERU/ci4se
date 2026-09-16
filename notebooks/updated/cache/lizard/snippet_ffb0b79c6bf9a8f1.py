def IsRunning(self):
    current_urn = self.Get(self.Schema.CURRENT_FLOW_URN)
    if not current_urn:
        return False
    try:
        current_flow = aff4.FACTORY.Open(urn=current_urn, aff4_type=flow.
            GRRFlow, token=self.token, mode='r')
    except aff4.InstantiationError:
        logging.error('Unable to open cron job run: %s', current_urn)
        self.DeleteAttribute(self.Schema.CURRENT_FLOW_URN)
        self.Flush()
        return False
    return current_flow.GetRunner().IsRunning()