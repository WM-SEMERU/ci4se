def rating(request):
    response = initial_validation(request, 'rating')
    if isinstance(response, HttpResponse):
        return response
    obj, post_data = response
    url = add_cache_bypass(obj.get_absolute_url().split('#')[0])
    response = redirect(url + '#rating-%s' % obj.id)
    rating_form = RatingForm(request, obj, post_data)
    if rating_form.is_valid():
        rating_form.save()
        if request.is_ajax():
            obj = obj.__class__.objects.get(id=obj.id)
            rating_name = obj.get_ratingfield_name()
            json = {}
            for f in ('average', 'count', 'sum'):
                json['rating_' + f] = getattr(obj, '%s_%s' % (rating_name, f))
            response = HttpResponse(dumps(json))
        if rating_form.undoing:
            ratings = set(rating_form.previous) ^ set([rating_form.current])
        else:
            ratings = rating_form.previous + [rating_form.current]
        set_cookie(response, 'yacms-rating', ','.join(ratings))
    return response