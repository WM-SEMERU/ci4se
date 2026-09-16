def encrypt(self, paddedMessage):
    if sys.version_info >= (3, 0) and not type(paddedMessage) in (bytes,
        bytearray) or type(paddedMessage) is unicode:
        paddedMessage = bytearray(paddedMessage.encode())
    else:
        paddedMessage = bytearray(paddedMessage)
    sessionRecord = self.sessionStore.loadSession(self.recipientId, self.
        deviceId)
    sessionState = sessionRecord.getSessionState()
    chainKey = sessionState.getSenderChainKey()
    messageKeys = chainKey.getMessageKeys()
    senderEphemeral = sessionState.getSenderRatchetKey()
    previousCounter = sessionState.getPreviousCounter()
    sessionVersion = sessionState.getSessionVersion()
    ciphertextBody = self.getCiphertext(sessionVersion, messageKeys,
        paddedMessage)
    ciphertextMessage = WhisperMessage(sessionVersion, messageKeys.
        getMacKey(), senderEphemeral, chainKey.getIndex(), previousCounter,
        ciphertextBody, sessionState.getLocalIdentityKey(), sessionState.
        getRemoteIdentityKey())
    if sessionState.hasUnacknowledgedPreKeyMessage():
        items = sessionState.getUnacknowledgedPreKeyMessageItems()
        localRegistrationid = sessionState.getLocalRegistrationId()
        ciphertextMessage = PreKeyWhisperMessage(sessionVersion,
            localRegistrationid, items.getPreKeyId(), items.
            getSignedPreKeyId(), items.getBaseKey(), sessionState.
            getLocalIdentityKey(), ciphertextMessage)
    sessionState.setSenderChainKey(chainKey.getNextChainKey())
    self.sessionStore.storeSession(self.recipientId, self.deviceId,
        sessionRecord)
    return ciphertextMessage