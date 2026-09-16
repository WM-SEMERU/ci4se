def get_active(slug=DEFAULT_TERMS_SLUG):
    active_terms = cache.get('tandc.active_terms_' + slug)
    if active_terms is None:
        try:
            active_terms = TermsAndConditions.objects.filter(
                date_active__isnull=False, date_active__lte=timezone.now(),
                slug=slug).latest('date_active')
            cache.set('tandc.active_terms_' + slug, active_terms,
                TERMS_CACHE_SECONDS)
        except TermsAndConditions.DoesNotExist:
            LOGGER.error(
                'Requested Terms and Conditions that Have Not Been Created.')
            return None
    return active_terms