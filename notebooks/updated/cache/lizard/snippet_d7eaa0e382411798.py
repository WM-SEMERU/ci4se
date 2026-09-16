def snake_to_camel_case(name):
    name = name.replace('-', '_')
    return ''.join(word.capitalize() for word in name.split('_'))