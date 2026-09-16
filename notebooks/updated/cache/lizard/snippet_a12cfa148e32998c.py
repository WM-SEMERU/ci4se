def report(location, document):
    assert isinstance(location, six.string_types)
    if location.endswith('.py'):
        return report_pyflakes(document)
    else:
        return []