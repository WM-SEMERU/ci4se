def has_tokens(self, phrase):
    if len(phrase) == 1 and classifier_options.is_special_class_word(phrase[0]
        ):
        return True
    tree = self.root
    for token in phrase:
        if not tree.has_child(token):
            return False
        tree = tree.get_child(token)
    return True if tree.is_end_of_phrase() else None