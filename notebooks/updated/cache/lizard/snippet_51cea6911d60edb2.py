def inject_documentation(**options):
    import cog
    loader = ConfigLoader(**options)
    cog.out('\n' + loader.documentation + '\n\n')