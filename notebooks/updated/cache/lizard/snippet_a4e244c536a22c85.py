def _remove_word(completer):

    def inner(word: str):
        try:
            completer.words.remove(word)
        except Exception:
            pass
    return inner