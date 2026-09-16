def current_user_was_last_verifier(analysis):
    verifiers = analysis.getVerificators()
    return verifiers and verifiers[:-1] == api.get_current_user().getId()