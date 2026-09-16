def retrieve_layers(self, *args, **options):
    queryset = Q()
    if len(args) < 1:
        all_layers = Layer.objects.published().external()
        if options['exclude']:
            exclude_list = options['exclude'].replace(' ', '').split(',')
            return all_layers.exclude(slug__in=exclude_list)
        else:
            self.verbose('no layer specified, will retrieve all layers!')
            return all_layers
    for layer_slug in args:
        queryset = queryset | Q(slug=layer_slug)
        try:
            layer = Layer.objects.get(slug=layer_slug)
            if not layer.is_external:
                raise CommandError(
                    'Layer "%s" is not an external layer\n\r' % layer_slug)
            if not layer.is_published:
                raise CommandError(
                    'Layer "%s" is not published. Why are you trying to work on an unpublished layer?\n\r'
                     % layer_slug)
        except Layer.DoesNotExist:
            raise CommandError('Layer "%s" does not exist\n\r' % layer_slug)
    return Layer.objects.published().external().select_related().filter(
        queryset)