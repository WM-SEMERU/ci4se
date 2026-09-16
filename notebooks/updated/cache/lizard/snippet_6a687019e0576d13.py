def predict(self, x):
    recurrent_unit = self.config['recurrent-unit-type']
    if recurrent_unit == 'lstm':
        context_state = self.encoder.predict(np.array(x))
    elif recurrent_unit == 'gru':
        hidden_state = self.encoder.predict(np.array(x))
        context_state = [hidden_state]
    else:
        raise Exception('Invalid recurrent unit type: {}'.format(
            recurrent_unit))
    y = self.vectorizer.vectorize_utterance([self.config['start']])
    response = []
    while True:
        output_token_probs = None
        if recurrent_unit == 'lstm':
            output_token_probs, h, c = self.decoder.predict([y] + context_state
                )
            context_state = [h, c]
        elif recurrent_unit == 'gru':
            output_token_probs, hidden_state = self.decoder.predict([y] +
                context_state)
            context_state = [hidden_state]
        else:
            raise Exception('Invalid recurrent unit type: {}'.format(
                recurrent_unit))
        sampled_token = np.argmax(output_token_probs[(0), (-1), :])
        response += [sampled_token]
        if sampled_token == self.vectorizer.ie.transform([self.config['stop']]
            ) or len(response) >= self.config['max-utterance-length']:
            break
        y = np.array([sampled_token])
    return response