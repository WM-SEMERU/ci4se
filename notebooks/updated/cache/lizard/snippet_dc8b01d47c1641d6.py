def execute(self, *args, **kwargs):
    try:
        return self.client.execute(*args, **kwargs)
    except requests.exceptions.HTTPError as err:
        res = err.response
        logger.error('%s response executing GraphQL.' % res.status_code)
        logger.error(res.text)
        self.display_gorilla_error_if_found(res)
        six.reraise(*sys.exc_info())