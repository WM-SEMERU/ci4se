def processV2(self, sessionRecord, message):
    if message.getPreKeyId() is None:
        raise InvalidKeyIdException('V2 message requires one time prekey id!')
    if not self.preKeyStore.containsPreKey(message.getPreKeyId()
        ) and self.sessionStore.containsSession(self.recipientId, self.deviceId
        ):
        logging.warn(
            "We've already processed the prekey part of this V2 session, letting bundled message fall through..."
            )
        return None
    ourPreKey = self.preKeyStore.loadPreKey(message.getPreKeyId()).getKeyPair()
    parameters = BobAxolotlParameters.newBuilder()
    parameters.setOurIdentityKey(self.identityKeyStore.getIdentityKeyPair()
        ).setOurSignedPreKey(ourPreKey).setOurRatchetKey(ourPreKey
        ).setOurOneTimePreKey(None).setTheirIdentityKey(message.
        getIdentityKey()).setTheirBaseKey(message.getBaseKey())
    if not sessionRecord.isFresh():
        sessionRecord.archiveCurrentState()
    RatchetingSession.initializeSessionAsBob(sessionRecord.getSessionState(
        ), message.getMessageVersion(), parameters.create())
    sessionRecord.getSessionState().setLocalRegistrationId(self.
        identityKeyStore.getLocalRegistrationId())
    sessionRecord.getSessionState().setRemoteRegistrationId(message.
        getRegistrationId())
    sessionRecord.getSessionState().setAliceBaseKey(message.getBaseKey().
        serialize())
    if message.getPreKeyId() != Medium.MAX_VALUE:
        return message.getPreKeyId()
    else:
        return None