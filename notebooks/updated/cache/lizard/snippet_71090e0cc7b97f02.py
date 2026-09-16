def cmd(send, msg, _):
    try:
        req = get('http://thefuckingweather.com/April/%s' % msg, timeout=5)
        doc = fromstring(req.text)
        elem = doc.find('.//h1')
    except ReadTimeout:
        elem = None
    if elem is None:
        send('NO FSCKING RESULTS.')
    else:
        send(elem.text)