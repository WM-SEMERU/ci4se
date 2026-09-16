def web(host, port):
    from .webserver.web import get_app
    get_app().run(host=host, port=port)