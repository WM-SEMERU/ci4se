def set_scf_initial_guess(self, guess='SAD'):
    availabel_guesses = {'core', 'sad', 'gwh', 'read', 'fragmo'}
    if guess.lower() not in availabel_guesses:
        raise ValueError('The guess method ' + guess + ' is not supported yet')
    self.params['rem']['scf_guess'] = guess.lower()