def _deliverAnswer(self, answer):
    router = self.siteRouter
    if answer.deliveryDeferred is None:
        d = answer.deliveryDeferred = router.routeAnswer(answer.
            originalSender, answer.originalTarget, answer.value, answer.
            messageID)

        def destroyAnswer(result):
            answer.deleteFromStore()

        def transportErrorCheck(f):
            answer.deliveryDeferred = None
            f.trap(MessageTransportError)
        d.addCallbacks(destroyAnswer, transportErrorCheck)
        d.addErrback(log.err)