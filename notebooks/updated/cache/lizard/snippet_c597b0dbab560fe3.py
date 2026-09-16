def create_app(*, debug=False, threads=1, bigchaindb_factory=None):
    if not bigchaindb_factory:
        bigchaindb_factory = BigchainDB
    app = Flask(__name__)
    app.wsgi_app = StripContentTypeMiddleware(app.wsgi_app)
    CORS(app)
    app.debug = debug
    app.config['bigchain_pool'] = utils.pool(bigchaindb_factory, size=threads)
    add_routes(app)
    return app