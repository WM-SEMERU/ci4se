def _verify_state(self, resp, state_data, state):
    is_known_state = 'state' in resp and 'state' in state_data and resp['state'
        ] == state_data['state']
    if not is_known_state:
        received_state = resp.get('state', '')
        satosa_logging(logger, logging.DEBUG, 
            'Missing or invalid state [%s] in response!' % received_state,
            state)
        raise SATOSAAuthenticationError(state, 
            'Missing or invalid state [%s] in response!' % received_state)