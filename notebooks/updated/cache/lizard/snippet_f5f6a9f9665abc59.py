def run_job_async(self, tgt, fun, arg=(), tgt_type='glob', ret='', timeout=
    None, jid='', kwarg=None, listen=True, io_loop=None, **kwargs):
    arg = salt.utils.args.parse_input(arg, kwargs=kwarg)
    try:
        pub_data = yield self.pub_async(tgt, fun, arg, tgt_type, ret, jid=
            jid, timeout=self._get_timeout(timeout), io_loop=io_loop,
            listen=listen, **kwargs)
    except SaltClientError:
        raise SaltClientError(
            'The salt master could not be contacted. Is master running?')
    except AuthenticationError as err:
        raise AuthenticationError(err)
    except AuthorizationError as err:
        raise AuthorizationError(err)
    except Exception as general_exception:
        raise SaltClientError(general_exception)
    raise tornado.gen.Return(self._check_pub_data(pub_data, listen=listen))