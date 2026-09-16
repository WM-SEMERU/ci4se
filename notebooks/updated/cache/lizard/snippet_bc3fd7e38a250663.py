def check(text):
    err = 'pinker.latin'
    msg = "Use English. '{}' is the preferred form."
    list = [['other things being equal', ['ceteris paribus']], [
        'among other things', ['inter alia']], ['in and of itself', [
        'simpliciter']], ['having made the necessary changes', [
        'mutatis mutandis']]]
    return preferred_forms_check(text, list, err, msg)