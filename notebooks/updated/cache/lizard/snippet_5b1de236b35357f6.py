def reportSuspiciousNode(self, nodeName: str, reason=None, code: int=None,
    offendingMsg=None):
    logger.warning(
        '{} raised suspicion on node {} for {}; suspicion code is {}'.
        format(self, nodeName, reason, code))
    if code in (s.code for s in (Suspicions.PPR_DIGEST_WRONG, Suspicions.
        PPR_REJECT_WRONG, Suspicions.PPR_TXN_WRONG, Suspicions.
        PPR_STATE_WRONG, Suspicions.PPR_PLUGIN_EXCEPTION, Suspicions.
        PPR_SUB_SEQ_NO_WRONG, Suspicions.PPR_NOT_FINAL, Suspicions.
        PPR_WITH_ORDERED_REQUEST, Suspicions.PPR_AUDIT_TXN_ROOT_HASH_WRONG,
        Suspicions.PPR_BLS_MULTISIG_WRONG, Suspicions.PPR_TIME_WRONG)):
        logger.display('{}{} got one of primary suspicions codes {}'.format
            (VIEW_CHANGE_PREFIX, self, code))
        self.view_changer.on_suspicious_primary(Suspicions.get_by_code(code))
    if offendingMsg:
        self.discard(offendingMsg, reason, logger.debug)