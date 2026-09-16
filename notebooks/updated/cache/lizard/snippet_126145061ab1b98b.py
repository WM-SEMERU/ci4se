def check(text):
    err = 'strunk_white.composition'
    msg = "Try '{}' instead of '{}'."
    bad_forms = [['dishonest', ['not honest']], ['trifling', [
        'not important']], ['forgot', ['did not remember']], ['ignored', [
        'did not pay (any )?attention to']], ['distrusted', [
        'did not have much confidence in']], ['whether', [
        'the question as to whether']], ['no doubt', [
        'there is no doubt but that']], ['used for fuel', [
        'used for fuel purposes']], ['he', ['he is a man who']], ['hastily',
        ['in a hasty manner']], ['this subject', ['this is a subject that']
        ], ['Her story is strange.', ['Her story is a strange one.']], [
        'because', ['the reason why is that']], ['because / since', [
        'owing to the fact that']], ['although / though', [
        'in spite of the fact that']], ['remind you / notify you', [
        'call your attention to the fact that']], [
        'I did not know that / I was unaware that', [
        'I was unaware of the fact that']], ['his failure', [
        'the fact that he had not succeeded']], ['my arrival', [
        'the fact that i had arrived']]]
    return preferred_forms_check(text, bad_forms, err, msg)