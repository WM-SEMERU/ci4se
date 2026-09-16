def validate_string(string, options=None):
    output.info('Performing JSON schema validation on input string: ' + string)
    stream = io.StringIO(string)
    return validate(stream, options)