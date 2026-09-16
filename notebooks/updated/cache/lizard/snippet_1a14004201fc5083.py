def sign_s3_upload(self):
    AWS_ACCESS_KEY = self.config_('AWS_ACCESS_KEY_ID')
    AWS_SECRET_KEY = self.config_('AWS_SECRET_ACCESS_KEY')
    S3_BUCKET = self.config_('AWS_S3_BUCKET_NAME')
    object_name = request.args.get('s3_object_name')
    mime_type = request.args.get('s3_object_type')
    expires = long(time.time() + 10)
    amz_headers = 'x-amz-acl:public-read'
    put_request = 'PUT\n\n%s\n%d\n%s\n/%s/%s' % (mime_type, expires,
        amz_headers, S3_BUCKET, object_name)
    signature = base64.encodestring(hmac.new(AWS_SECRET_KEY, put_request,
        sha1).digest())
    signature = urllib.quote(urllib.quote_plus(signature.strip()))
    url = 'https://s3.amazonaws.com/%s/%s' % (S3_BUCKET, object_name)
    return jsonify({'signed_request': 
        '%s?AWSAccessKeyId=%s&Expires=%d&Signature=%s' % (url,
        AWS_ACCESS_KEY, expires, signature), 'url': url})