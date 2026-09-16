def init_app(self, app):
    if not hasattr(app, 'extensions'):
        app.extensions = {}
    app.extensions['imagine'] = self
    self._set_defaults(app)
    self._redirect_code = app.config['IMAGINE_CACHE_REDIRECT_CODE']
    if isinstance(app.config['IMAGINE_ADAPTERS'], dict):
        self._adapters.update(app.config['IMAGINE_ADAPTERS'])
    if isinstance(app.config['IMAGINE_FILTERS'], dict):
        self._filters.update(app.config['IMAGINE_FILTERS'])
    self._handle_adapter(app)
    self._handle_filter_sets(app)
    self._add_url_rule(app)