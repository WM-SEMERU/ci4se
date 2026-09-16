def letter():

    @Parser
    def letter_parser(text, index=0):
        if index < len(text) and text[index].isalpha():
            return Value.success(index + 1, text[index])
        else:
            return Value.failure(index, 'a letter')
    return letter_parser