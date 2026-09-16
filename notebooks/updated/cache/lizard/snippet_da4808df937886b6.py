def blog_post_feed(request, format, **kwargs):
    try:
        return {'rss': PostsRSS, 'atom': PostsAtom}[format](**kwargs)(request)
    except KeyError:
        raise Http404()