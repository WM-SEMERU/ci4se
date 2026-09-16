def view_quick_save_page(name=None):
    response.set_header('Cache-control', 'no-cache')
    response.set_header('Pragma', 'no-cache')
    if request.method == 'PUT':
        if name is None:
            if len(request.forms.filename) > 0:
                name = request.forms.filename
        if name is not None:
            filename = '{0}.rst'.format(name)
            file_handle = open(filename, 'w')
            content = request.body.read()
            content = content.decode('utf-8')
            file_handle.write(content.encode('utf-8'))
            file_handle.close()
            return 'OK'
        else:
            return abort(404)