def rate(self, rating):
    parameters = {'voterid': self._current_user_id, 'target_userid': self.
        id, 'type': 'vote', 'cf': 'profile2', 'target_objectid': 0,
        'vote_type': 'personality', 'score': rating}
    response = self._session.okc_post('vote_handler', data=parameters)
    response_json = response.json()
    log_function = log.info if response_json.get('status', False
        ) else log.error
    log_function(simplejson.dumps({'rate_response': response_json,
        'sent_parameters': parameters, 'headers': dict(self._session.headers)})
        )
    self.refresh(reload=False)