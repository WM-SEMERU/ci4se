def upload_file(fapi, file_name, conf):
    if not conf.has_key('file-type'):
        raise SmarterlingError("%s doesn't have a file-type" % file_name)
    print('Uploading %s to smartling' % file_name)
    data = UploadData(os.path.dirname(file_name) + os.sep, os.path.basename
        (file_name), conf.get('file-type'))
    data.setUri(file_uri(file_name, conf))
    if conf.has_key('approve-content'):
        data.setApproveContent('true' if conf.get('approve-content', True) else
            'false')
    if conf.has_key('callback-url'):
        data.setCallbackUrl(conf.get('callback-url'))
    for name, value in conf.get('directives', {}).items():
        data.addDirective(SmartlingDirective(name, value))
    response, code = fapi.upload(data)
    if code != 200:
        print(repr(response))
        raise SmarterlingError('Error uploading file: %s' % file_name)
    else:
        print('Uploaded %s, wordCount: %s, stringCount: %s' % (file_name,
            response.data.wordCount, response.data.stringCount))