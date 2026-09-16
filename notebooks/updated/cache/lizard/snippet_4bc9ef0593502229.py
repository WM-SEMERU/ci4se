def make_application():
    settings = {}
    application = web.Application([web.url('/', SimpleHandler)], **settings)
    statsd.install(application, **{'namespace': 'testing'})
    return application