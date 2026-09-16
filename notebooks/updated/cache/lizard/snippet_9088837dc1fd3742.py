def verify_request_signature(request: RequestType, public_key: Union[str,
    bytes]):
    key = encode_if_text(public_key)
    date_header = request.headers.get('Date')
    if not date_header:
        raise ValueError('Rquest Date header is missing')
    ts = parse_http_date(date_header)
    dt = datetime.datetime.utcfromtimestamp(ts).replace(tzinfo=pytz.utc)
    delta = datetime.timedelta(seconds=30)
    now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
    if dt < now - delta or dt > now + delta:
        raise ValueError('Request Date is too far in future or past')
    HTTPSignatureHeaderAuth.verify(request, key_resolver=lambda **kwargs: key)