def view_404(request, url=None):
    res = render_to_response('404.html', {'PAGE_URL': request.get_full_path
        ()}, context_instance=RequestContext(request))
    res.status_code = 404
    return res