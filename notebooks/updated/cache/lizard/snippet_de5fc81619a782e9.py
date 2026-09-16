def update(self, friendly_name=values.unset, chat_service_sid=values.unset,
    channel_type=values.unset, contact_identity=values.unset, enabled=
    values.unset, integration_type=values.unset, integration_flow_sid=
    values.unset, integration_url=values.unset, integration_workspace_sid=
    values.unset, integration_workflow_sid=values.unset,
    integration_channel=values.unset, integration_timeout=values.unset,
    integration_priority=values.unset, integration_creation_on_message=
    values.unset, long_lived=values.unset):
    data = values.of({'FriendlyName': friendly_name, 'ChatServiceSid':
        chat_service_sid, 'ChannelType': channel_type, 'ContactIdentity':
        contact_identity, 'Enabled': enabled, 'IntegrationType':
        integration_type, 'Integration.FlowSid': integration_flow_sid,
        'Integration.Url': integration_url, 'Integration.WorkspaceSid':
        integration_workspace_sid, 'Integration.WorkflowSid':
        integration_workflow_sid, 'Integration.Channel':
        integration_channel, 'Integration.Timeout': integration_timeout,
        'Integration.Priority': integration_priority,
        'Integration.CreationOnMessage': integration_creation_on_message,
        'LongLived': long_lived})
    payload = self._version.update('POST', self._uri, data=data)
    return FlexFlowInstance(self._version, payload, sid=self._solution['sid'])