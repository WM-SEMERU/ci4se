def check(text):
    err = 'glaad.terms'
    msg = "Possibly offensive term. Consider using '{}' instead of '{}'."
    list = [['gay man', ['homosexual man']], ['gay men', ['homosexual men']
        ], ['lesbian', ['homosexual woman']], ['lesbians', [
        'homosexual women']], ['gay people', ['homosexual people']], [
        'gay couple', ['homosexual couple']], ['sexual orientation', [
        'sexual preference']], ['openly gay', ['admitted homosexual',
        'avowed homosexual']], ['equal rights', ['special rights']]]
    return preferred_forms_check(text, list, err, msg, ignore_case=False)