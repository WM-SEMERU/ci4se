def callRemote(self, objectPath, methodName, interface=None, destination=
    None, signature=None, body=None, expectReply=True, autoStart=True,
    timeout=None, returnSignature=_NO_CHECK_RETURN):
    try:
        mcall = message.MethodCallMessage(objectPath, methodName, interface
            =interface, destination=destination, signature=signature, body=
            body, expectReply=expectReply, autoStart=autoStart, oobFDs=self
            ._toBeSentFDs)
        d = self.callRemoteMessage(mcall, timeout)
        d.addCallback(self._cbCvtReply, returnSignature)
        return d
    except Exception:
        return defer.fail()