def _IsIdentifier(cls, string):
    return string and not string[0].isdigit() and all(character.isalnum() or
        character == '_' for character in string)