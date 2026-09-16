def specification(cls, *context_specs):
    import_data = []
    for name in context_specs:
        import_data.append((name, None))
    return cls.import_context(import_data)