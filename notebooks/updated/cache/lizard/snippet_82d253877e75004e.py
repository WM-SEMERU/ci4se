def wrapped_request(self, request, *args, **kwargs):
    f = tornado_Future()
    try:
        use_mid = kwargs.get('use_mid')
        timeout = kwargs.get('timeout')
        mid = kwargs.get('mid')
        msg = Message.request(request, *args, mid=mid)
    except Exception:
        f.set_exc_info(sys.exc_info())
        return f
    return transform_future(self.reply_wrapper, self.katcp_client.
        future_request(msg, timeout, use_mid))