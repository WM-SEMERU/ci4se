def rpXRDS(request):
    return util.renderXRDS(request, [RP_RETURN_TO_URL_TYPE], [util.
        getViewURL(request, finishOpenID)])