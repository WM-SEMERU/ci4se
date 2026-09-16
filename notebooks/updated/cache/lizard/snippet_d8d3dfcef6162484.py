def camelHump(text):
    output = ''.join([(word[0].upper() + word[1:]) for word in words(text)])
    if output:
        output = output[0].lower() + output[1:]
    return output