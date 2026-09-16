def group_create_session(self, groupid, participantid, skmsgdata):
    logger.debug(
        'group_create_session(groupid=%s, participantid=%s, skmsgdata=[omitted])'
         % (groupid, participantid))
    senderKeyName = SenderKeyName(groupid, AxolotlAddress(participantid, 0))
    senderkeydistributionmessage = SenderKeyDistributionMessage(serialized=
        skmsgdata)
    self._group_session_builder.process(senderKeyName,
        senderkeydistributionmessage)