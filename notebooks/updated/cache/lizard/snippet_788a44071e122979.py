def get_handler(self, *args, **options):
    handler = super(Command, self).get_handler(*args, **options)
    if options['use_livereload']:
        self.livereload_request(**options)
    return handler