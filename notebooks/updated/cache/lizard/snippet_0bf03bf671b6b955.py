def portrait_image(model, request):
    response = Response()
    cfg = ugm_general(model)
    response.body = model.attrs[cfg.attrs['users_portrait_attr']]
    response.headers['Content-Type'] = 'image/jpeg'
    response.headers['Cache-Control'] = 'max-age=0'
    return response