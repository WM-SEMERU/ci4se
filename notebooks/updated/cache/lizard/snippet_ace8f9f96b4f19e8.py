def check(text):
    err = 'redundancy.wallace'
    msg = "Redundancy. Use '{}' instead of '{}'."
    redundancies = [['rectangular', ['rectangular in shape']], ['audible',
        ['audible to the ear']]]
    return preferred_forms_check(text, redundancies, err, msg)