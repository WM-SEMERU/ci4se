def OnStartup(self):
    last_request = self.transaction_log.Get()
    if last_request:
        status = rdf_flows.GrrStatus(status=rdf_flows.GrrStatus.
            ReturnedStatus.CLIENT_KILLED, error_message=
            'Client killed during transaction')
        if self.nanny_controller:
            nanny_status = self.nanny_controller.GetNannyStatus()
            if nanny_status:
                status.nanny_status = nanny_status
        self.SendReply(status, request_id=last_request.request_id,
            response_id=1, session_id=last_request.session_id, message_type
            =rdf_flows.GrrMessage.Type.STATUS)
    self.transaction_log.Clear()
    action = admin.SendStartupInfo(grr_worker=self)
    action.Run(None, ttl=1)