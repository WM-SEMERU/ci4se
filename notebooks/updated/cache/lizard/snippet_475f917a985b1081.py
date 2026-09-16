def UpdateFlows(self, client_id_flow_id_pairs, pending_termination=db.
    Database.unchanged):
    for client_id, flow_id in client_id_flow_id_pairs:
        try:
            self.UpdateFlow(client_id, flow_id, pending_termination=
                pending_termination)
        except db.UnknownFlowError:
            pass