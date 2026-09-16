def handleOneClientMsg(self, wrappedMsg):
    try:
        vmsg = self.validateClientMsg(wrappedMsg)
        if vmsg:
            self.unpackClientMsg(*vmsg)
    except BlowUp:
        raise
    except Exception as ex:
        msg, frm = wrappedMsg
        friendly = friendlyEx(ex)
        if isinstance(ex, SuspiciousClient):
            self.reportSuspiciousClient(frm, friendly)
        self.handleInvalidClientMsg(ex, wrappedMsg)