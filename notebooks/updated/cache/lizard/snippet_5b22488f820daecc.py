def _normalize_helper(number, replacements, remove_non_matches):
    normalized_number = []
    for char in number:
        new_digit = replacements.get(char.upper(), None)
        if new_digit is not None:
            normalized_number.append(new_digit)
        elif not remove_non_matches:
            normalized_number.append(char)
    return U_EMPTY_STRING.join(normalized_number)