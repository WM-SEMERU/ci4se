def start_http_server(self, port, host='0.0.0.0', endpoint='/metrics'):
    if is_running_from_reloader():
        return
    app = Flask('prometheus-flask-exporter-%d' % port)
    self.register_endpoint(endpoint, app)

    def run_app():
        app.run(host=host, port=port)
    thread = threading.Thread(target=run_app)
    thread.setDaemon(True)
    thread.start()