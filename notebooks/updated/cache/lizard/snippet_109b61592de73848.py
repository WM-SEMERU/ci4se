def _RunAction(self, rule, client_id):
    actions_count = 0
    try:
        if self._CheckIfHuntTaskWasAssigned(client_id, rule.hunt_id):
            logging.info(
                'Foreman: ignoring hunt %s on client %s: was started here before'
                , client_id, rule.hunt_id)
        else:
            logging.info('Foreman: Starting hunt %s on client %s.', rule.
                hunt_id, client_id)
            if rule.hunt_name:
                flow_cls = registry.AFF4FlowRegistry.FlowClassByName(rule.
                    hunt_name)
                hunt_urn = rdfvalue.RDFURN('aff4:/hunts/%s' % rule.hunt_id)
                flow_cls.StartClients(hunt_urn, [client_id])
            else:
                hunt.StartHuntFlowOnClient(client_id, rule.hunt_id)
            actions_count += 1
    except Exception as e:
        logging.exception('Failure running foreman action on client %s: %s',
            rule.hunt_id, e)
    return actions_count